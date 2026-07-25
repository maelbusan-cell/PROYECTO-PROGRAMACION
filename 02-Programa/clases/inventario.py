from estructuras.lista_circular import ListaCircular
from estructuras.cola import Cola
from estructuras.pila import Pila
from algoritmos.ordenamiento import burbuja, merge_sort
from algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from clases.producto import Producto, ProductoPerecedero, ProductoNoPerecedero
from clases.proveedor import Proveedor
from clases.movimiento import Entrada, Salida
from datetime import datetime


class Inventario:
    def __init__(self, db=None):
        self._lista_circular = ListaCircular()
        self._cola_pedidos = Cola()
        self._pila_movimientos = Pila()
        self._proveedores = {}
        self._db = db
        self._cargar_datos()

    @property
    def lista_circular(self):
        return self._lista_circular

    @property
    def cola_pedidos(self):
        return self._cola_pedidos

    @property
    def pila_movimientos(self):
        return self._pila_movimientos

    @property
    def proveedores(self):
        return self._proveedores

    def _cargar_datos(self):
        if not self._db:
            return
        self._db.conectar()
        self._db.crear_tablas()
        filas = self._db.obtener("SELECT * FROM productos")
        for f in filas:
            cod, nom, cat, pre, stock, smin, smax, tipo, dias, gar = f
            if tipo == "Perecedero":
                p = ProductoPerecedero(cod, nom, cat or "", pre, stock, dias or 0, smin, smax)
            elif tipo == "No perecedero":
                p = ProductoNoPerecedero(cod, nom, cat or "", pre, stock, gar or 0, smin, smax)
            else:
                p = Producto(cod, nom, cat or "", pre, stock, smin, smax)
            self._lista_circular.insertar(p)
        filas = self._db.obtener("SELECT * FROM proveedores")
        for f in filas:
            ruc, nom, tel, email, dirr = f
            self._proveedores[ruc] = Proveedor(ruc, nom, tel or "", email or "", dirr or "")

    def _guardar_producto_db(self, p):
        if not self._db:
            return
        self._db.ejecutar(
            "INSERT OR REPLACE INTO productos VALUES (?,?,?,?,?,?,?,?,?,?)",
            (p.codigo, p.nombre, p.categoria, p.precio, p.stock_actual,
             p._stock_minimo, p._stock_maximo, p.tipo(),
             getattr(p, '_dias_caducidad', None),
             getattr(p, '_garantia_meses', None)))

    def _guardar_proveedor_db(self, p):
        if not self._db:
            return
        self._db.ejecutar(
            "INSERT OR REPLACE INTO proveedores VALUES (?,?,?,?,?)",
            (p.ruc, p.nombre, p.telefono, p.email, p.direccion))

    def _guardar_movimiento_db(self, m, proveedor_ruc=None, destino=None):
        if not self._db:
            return
        self._db.ejecutar(
            "INSERT INTO movimientos (tipo, codigo_producto, cantidad, fecha, proveedor_ruc, destino) VALUES (?,?,?,?,?,?)",
            (m.tipo_movimiento(), m.producto.codigo, m.cantidad,
             m.fecha.strftime('%Y-%m-%d %H:%M:%S'), proveedor_ruc, destino))

    def registrar_producto(self, producto):
        self._lista_circular.insertar(producto)
        self._guardar_producto_db(producto)

    def eliminar_producto(self, codigo):
        prod = self._lista_circular.eliminar(codigo)
        if prod and self._db:
            self._db.ejecutar("DELETE FROM productos WHERE codigo = ?", (codigo,))
        return prod

    def buscar_producto(self, codigo):
        return self._lista_circular.buscar(codigo)

    def listar_productos(self):
        return self._lista_circular.recorrer()

    def registrar_proveedor(self, proveedor):
        self._proveedores[proveedor.ruc] = proveedor
        self._guardar_proveedor_db(proveedor)

    def eliminar_proveedor(self, ruc):
        if ruc in self._proveedores:
            del self._proveedores[ruc]
            if self._db:
                self._db.ejecutar("DELETE FROM proveedores WHERE ruc = ?", (ruc,))
            return True
        return False

    def listar_proveedores(self):
        return list(self._proveedores.values())

    def listar_movimientos(self):
        return self._pila_movimientos.listar()

    def entrada_mercancia(self, movimiento, proveedor_ruc=None):
        movimiento.procesar()
        self._pila_movimientos.push(movimiento)
        self._guardar_movimiento_db(movimiento, proveedor_ruc=proveedor_ruc)
        self._guardar_producto_db(movimiento.producto)

    def salida_mercancia(self, movimiento, destino=None):
        movimiento.procesar()
        self._pila_movimientos.push(movimiento)
        self._guardar_movimiento_db(movimiento, destino=destino)
        self._guardar_producto_db(movimiento.producto)

    def deshacer_movimiento(self):
        mov = self._pila_movimientos.pop()
        if mov:
            mov.deshacer()
            self._guardar_producto_db(mov.producto)
            if self._db:
                self._db.ejecutar(
                    "DELETE FROM movimientos WHERE id = (SELECT MAX(id) FROM movimientos)")
        return mov

    def agregar_pedido(self, pedido):
        self._cola_pedidos.enqueue(pedido)

    def procesar_pedido(self):
        return self._cola_pedidos.dequeue()

    def reporte_bajo_stock(self):
        productos = self._lista_circular.recorrer()
        return [p for p in productos if p.stock_actual <= p._stock_minimo]

    def rotar_inventario(self):
        self._lista_circular.rotar()

    def ordenar_burbuja(self, criterio="codigo"):
        claves = {"codigo": lambda p: p.codigo,
                  "nombre": lambda p: p.nombre.lower(),
                  "precio": lambda p: p.precio,
                  "stock":  lambda p: p.stock_actual}
        key = claves.get(criterio, claves["codigo"])
        return burbuja(self._lista_circular.recorrer(), key)

    def ordenar_merge(self, criterio="codigo"):
        claves = {"codigo": lambda p: p.codigo,
                  "nombre": lambda p: p.nombre.lower(),
                  "precio": lambda p: p.precio,
                  "stock":  lambda p: p.stock_actual}
        key = claves.get(criterio, claves["codigo"])
        return merge_sort(self._lista_circular.recorrer(), key)

    def buscar_lineal_por_nombre(self, nombre):
        lista = self._lista_circular.recorrer()
        return busqueda_lineal(lista, nombre.lower(), key=lambda p: p.nombre.lower())

    def buscar_binaria_por_codigo(self, codigo):
        lista = self.ordenar_merge("codigo")
        return busqueda_binaria(lista, codigo, key=lambda p: p.codigo)
