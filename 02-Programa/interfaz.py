import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, ttk
import sqlite3
import os
from abc import ABC, abstractmethod
from datetime import datetime


def burbuja(lista, key=lambda x: x):
    copia = lista[:]
    n = len(copia)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if key(copia[j]) > key(copia[j + 1]):
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia


def merge_sort(lista, key=lambda x: x):
    if len(lista) <= 1:
        return lista[:]
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio], key)
    der = merge_sort(lista[medio:], key)
    return _merge(izq, der, key)


def _merge(izq, der, key):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if key(izq[i]) <= key(der[j]):
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def busqueda_lineal(lista, valor, key=lambda x: x):
    for i, item in enumerate(lista):
        if key(item) == valor:
            return i, item
    return -1, None


def busqueda_binaria(lista, valor, key=lambda x: x):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        val_medio = key(lista[medio])
        if val_medio == valor:
            return medio, lista[medio]
        elif val_medio < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1, None


class Nodo:
    def __init__(self, dato):
        self._dato = dato
        self._siguiente = None
        self._anterior = None

    @property
    def dato(self):
        return self._dato

    @dato.setter
    def dato(self, valor):
        self._dato = valor

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, valor):
        self._siguiente = valor

    @property
    def anterior(self):
        return self._anterior

    @anterior.setter
    def anterior(self, valor):
        self._anterior = valor


class ListaCircular:
    def __init__(self):
        self._ultimo = None
        self._tamano = 0

    @property
    def ultimo(self):
        return self._ultimo

    @property
    def tamano(self):
        return self._tamano

    def esta_vacia(self):
        return self._ultimo is None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self._ultimo = nuevo
        else:
            primero = self._ultimo.siguiente
            nuevo.siguiente = primero
            nuevo.anterior = self._ultimo
            primero.anterior = nuevo
            self._ultimo.siguiente = nuevo
        self._tamano += 1

    def eliminar(self, codigo):
        if self.esta_vacia():
            return None
        actual = self._ultimo.siguiente
        for _ in range(self._tamano):
            if actual.dato.codigo == codigo:
                if self._tamano == 1:
                    self._ultimo = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    if actual == self._ultimo:
                        self._ultimo = actual.anterior
                self._tamano -= 1
                return actual.dato
            actual = actual.siguiente
        return None

    def buscar(self, codigo):
        if self.esta_vacia():
            return None
        actual = self._ultimo.siguiente
        for _ in range(self._tamano):
            if actual.dato.codigo == codigo:
                return actual.dato
            actual = actual.siguiente
        return None

    def recorrer(self):
        if self.esta_vacia():
            return []
        resultado = []
        actual = self._ultimo.siguiente
        for _ in range(self._tamano):
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def rotar(self):
        if self._ultimo is not None:
            self._ultimo = self._ultimo.siguiente


class Cola:
    def __init__(self):
        self._frente = None
        self._final = None
        self._tamano = 0

    @property
    def tamano(self):
        return self._tamano

    def esta_vacia(self):
        return self._frente is None

    def enqueue(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._frente = nuevo
            self._final = nuevo
        else:
            self._final.siguiente = nuevo
            self._final = nuevo
        self._tamano += 1

    def dequeue(self):
        if self.esta_vacia():
            return None
        dato = self._frente.dato
        self._frente = self._frente.siguiente
        if self._frente is None:
            self._final = None
        self._tamano -= 1
        return dato

    def peek(self):
        if self.esta_vacia():
            return None
        return self._frente.dato

    def listar(self):
        if self.esta_vacia():
            return []
        resultado = []
        actual = self._frente
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado


class Pila:
    def __init__(self):
        self._tope = None
        self._tamano = 0

    @property
    def tamano(self):
        return self._tamano

    def esta_vacia(self):
        return self._tope is None

    def push(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self._tope
        self._tope = nuevo
        self._tamano += 1

    def pop(self):
        if self.esta_vacia():
            return None
        dato = self._tope.dato
        self._tope = self._tope.siguiente
        self._tamano -= 1
        return dato

    def peek(self):
        if self.esta_vacia():
            return None
        return self._tope.dato

    def listar(self):
        if self.esta_vacia():
            return []
        resultado = []
        actual = self._tope
        while actual is not None:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado


class ConexionDB:
    def __init__(self, ruta=None):
        if ruta is None:
            ruta = os.path.join(os.path.dirname(__file__), "inventario.db")
        self._ruta = ruta
        self._conn = None

    def conectar(self):
        self._conn = sqlite3.connect(self._ruta)
        self._conn.execute("PRAGMA foreign_keys = ON")
        return self._conn

    def desconectar(self):
        if self._conn:
            self._conn.close()

    def ejecutar(self, consulta, parametros=None):
        c = self._conn.cursor()
        if parametros:
            c.execute(consulta, parametros)
        else:
            c.execute(consulta)
        self._conn.commit()
        return c

    def obtener(self, consulta, parametros=None):
        c = self._conn.cursor()
        if parametros:
            c.execute(consulta, parametros)
        else:
            c.execute(consulta)
        return c.fetchall()

    def crear_tablas(self):
        self.ejecutar("""
            CREATE TABLE IF NOT EXISTS proveedores (
                ruc TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                telefono TEXT,
                email TEXT,
                direccion TEXT
            )
        """)
        self.ejecutar("""
            CREATE TABLE IF NOT EXISTS productos (
                codigo TEXT PRIMARY KEY,
                nombre TEXT NOT NULL,
                categoria TEXT,
                precio REAL NOT NULL,
                stock_actual INTEGER DEFAULT 0,
                stock_minimo INTEGER DEFAULT 0,
                stock_maximo INTEGER DEFAULT 999,
                tipo TEXT DEFAULT 'Producto',
                dias_caducidad INTEGER,
                garantia_meses INTEGER
            )
        """)
        self.ejecutar("""
            CREATE TABLE IF NOT EXISTS movimientos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT NOT NULL,
                codigo_producto TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                proveedor_ruc TEXT,
                destino TEXT,
                FOREIGN KEY (codigo_producto) REFERENCES productos(codigo),
                FOREIGN KEY (proveedor_ruc) REFERENCES proveedores(ruc)
            )
        """)


class Registrable(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass


class Producto(Registrable):
    def __init__(self, codigo, nombre, categoria, precio,
                 stock_actual, stock_minimo=0, stock_maximo=999):
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._stock_actual = stock_actual
        self._stock_minimo = stock_minimo
        self._stock_maximo = stock_maximo

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self._precio = valor

    @property
    def stock_actual(self):
        return self._stock_actual

    @stock_actual.setter
    def stock_actual(self, valor):
        if valor >= 0:
            self._stock_actual = valor

    def ajustar_stock(self, cantidad, motivo=None):
        self._stock_actual += cantidad
        if self._stock_actual < 0:
            self._stock_actual = 0

    def tipo(self):
        return "Producto"

    def mostrar_info(self):
        return (f"[{self._codigo}] {self._nombre} | "
                f"{self._categoria} | ${self._precio:.2f} | "
                f"Stock: {self._stock_actual}")


class ProductoPerecedero(Producto):
    def __init__(self, codigo, nombre, categoria, precio,
                 stock_actual, dias_caducidad, stock_minimo=0, stock_maximo=999):
        super().__init__(codigo, nombre, categoria, precio,
                         stock_actual, stock_minimo, stock_maximo)
        self._dias_caducidad = dias_caducidad

    @property
    def dias_caducidad(self):
        return self._dias_caducidad

    def tipo(self):
        return "Perecedero"

    def mostrar_info(self):
        return (super().mostrar_info() +
                f" | Caduca en: {self._dias_caducidad} días")


class ProductoNoPerecedero(Producto):
    def __init__(self, codigo, nombre, categoria, precio,
                 stock_actual, garantia_meses=0, stock_minimo=0, stock_maximo=999):
        super().__init__(codigo, nombre, categoria, precio,
                         stock_actual, stock_minimo, stock_maximo)
        self._garantia_meses = garantia_meses

    @property
    def garantia_meses(self):
        return self._garantia_meses

    def tipo(self):
        return "No perecedero"


class Proveedor(Registrable):
    def __init__(self, ruc, nombre, telefono, email, direccion):
        self._ruc = ruc
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._direccion = direccion

    @property
    def ruc(self):
        return self._ruc

    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono

    @property
    def email(self):
        return self._email

    @property
    def direccion(self):
        return self._direccion

    def mostrar_info(self):
        return (f"[{self._ruc}] {self._nombre} | "
                f"Tel: {self._telefono} | {self._email}")


class MovimientoInventario(ABC):
    def __init__(self, producto, cantidad):
        self._producto = producto
        self._cantidad = cantidad
        self._fecha = datetime.now()
        self._aplicado = False

    @property
    def producto(self):
        return self._producto

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def fecha(self):
        return self._fecha

    def resumen(self):
        signo = "+" if self._cantidad > 0 else ""
        return (f"{self._fecha.strftime('%d/%m/%Y %H:%M')} | "
                f"{self.tipo_movimiento()} | {self._producto.nombre} | "
                f"{signo}{self._cantidad}")

    @abstractmethod
    def procesar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass

    @abstractmethod
    def tipo_movimiento(self):
        pass


class Entrada(MovimientoInventario):
    def __init__(self, producto, cantidad, proveedor=None):
        super().__init__(producto, cantidad)
        self._proveedor = proveedor

    def procesar(self):
        self._producto.ajustar_stock(self._cantidad, motivo="Entrada")
        self._aplicado = True

    def deshacer(self):
        self._producto.ajustar_stock(-self._cantidad, motivo="Deshacer entrada")
        self._aplicado = False

    def tipo_movimiento(self):
        return "Entrada"


class Salida(MovimientoInventario):
    def __init__(self, producto, cantidad, destino=None):
        super().__init__(producto, cantidad)
        self._destino = destino

    def procesar(self):
        self._producto.ajustar_stock(-self._cantidad, motivo="Salida")
        self._aplicado = True

    def deshacer(self):
        self._producto.ajustar_stock(self._cantidad, motivo="Deshacer salida")
        self._aplicado = False

    def tipo_movimiento(self):
        return "Salida"


class Pedido:
    def __init__(self, id_pedido, cliente):
        self._id_pedido = id_pedido
        self._cliente = cliente
        self._productos = {}
        self._estado = "Pendiente"
        self._fecha = datetime.now()

    @property
    def id_pedido(self):
        return self._id_pedido

    @property
    def cliente(self):
        return self._cliente

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    @property
    def fecha(self):
        return self._fecha

    def agregar_producto(self, producto, cantidad):
        if producto.codigo in self._productos:
            self._productos[producto.codigo]["cantidad"] += cantidad
        else:
            self._productos[producto.codigo] = {
                "producto": producto,
                "cantidad": cantidad
            }

    def calcular_total(self):
        return sum(
            item["producto"].precio * item["cantidad"]
            for item in self._productos.values()
        )

    def mostrar_info(self):
        lineas = [f"Pedido #{self._id_pedido} | {self._cliente} | {self._estado}"]
        for item in self._productos.values():
            p = item["producto"]
            lineas.append(f"  - {p.nombre} x{item['cantidad']} = ${p.precio * item['cantidad']:.2f}")
        lineas.append(f"  TOTAL: ${self.calcular_total():.2f}")
        return "\n".join(lineas)


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


class VentanaPrincipal:
    def __init__(self, inventario):
        self._inventario = inventario
        self._contador_pedidos = 0
        self._ventana = tk.Tk()
        self._ventana.title("Inventario y Bodega - Grupo 7")
        self._ventana.geometry("750x500")
        self._configurar()

    def _configurar(self):
        marco = ttk.Frame(self._ventana)
        marco.pack(pady=10, fill=tk.X)

        # PRODUCTOS
        g1 = ttk.LabelFrame(marco, text="Productos", padding=5)
        g1.pack(side=tk.LEFT, padx=5)
        ttk.Button(g1, text="Registrar Producto", command=self._reg_producto, width=18).pack(pady=2)
        ttk.Button(g1, text="Listar Productos", command=self._listar, width=18).pack(pady=2)
        ttk.Button(g1, text="Buscar Producto", command=self._buscar, width=18).pack(pady=2)

        # INVENTARIO
        g2 = ttk.LabelFrame(marco, text="Inventario", padding=5)
        g2.pack(side=tk.LEFT, padx=5)
        ttk.Button(g2, text="Entrada/Salida", command=self._movimiento, width=18).pack(pady=2)
        ttk.Button(g2, text="Deshacer", command=self._deshacer, width=18).pack(pady=2)
        ttk.Button(g2, text="Bajo Stock", command=self._bajo_stock, width=18).pack(pady=2)

        # PEDIDOS
        g3 = ttk.LabelFrame(marco, text="Pedidos", padding=5)
        g3.pack(side=tk.LEFT, padx=5)
        ttk.Button(g3, text="Nuevo Pedido", command=self._pedido, width=18).pack(pady=2)
        ttk.Button(g3, text="Procesar Pedido", command=self._procesar_pedido, width=18).pack(pady=2)

        self._output = scrolledtext.ScrolledText(self._ventana, height=20, font=("Consolas", 10))
        self._output.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        ttk.Button(self._ventana, text="Salir", command=self._ventana.quit).pack(pady=5)

    def _mostrar(self, texto):
        self._output.insert(tk.END, texto + "\n")
        self._output.see(tk.END)

    def _reg_producto(self):
        cod = simpledialog.askstring("Producto", "Codigo:")
        if not cod: return
        nom = simpledialog.askstring("Producto", "Nombre:")
        if not nom: return
        cat = simpledialog.askstring("Producto", "Categoria:") or ""
        try:
            pre = float(simpledialog.askstring("Producto", "Precio:") or 0)
            stock = int(simpledialog.askstring("Producto", "Stock actual:") or 0)
            smin = int(simpledialog.askstring("Producto", "Stock minimo (0):") or 0)
            smax = int(simpledialog.askstring("Producto", "Stock maximo (999):") or 999)
        except:
            messagebox.showerror("Error", "Valores numericos invalidos")
            return

        self._inventario.registrar_producto(Producto(cod, nom, cat, pre, stock, smin, smax))
        self._mostrar(f"OK Producto registrado: {cod} - {nom}")

    def _listar(self):
        prods = self._inventario.ordenar_burbuja("codigo")
        self._mostrar("=== PRODUCTOS (Burbuja O(n2)) ===")
        if not prods:
            self._mostrar("(vacio)")
        for p in prods:
            self._mostrar(p.mostrar_info())

    def _buscar(self):
        tipo = simpledialog.askstring("Buscar", "Buscar por (codigo/nombre):")
        if not tipo: return
        if tipo.strip().lower() == "codigo":
            cod = simpledialog.askstring("Buscar", "Codigo del producto:")
            if not cod: return
            idx, prod = self._inventario.buscar_binaria_por_codigo(cod.strip())
            if prod:
                self._mostrar(f"Encontrado en posicion {idx}")
                self._mostrar(prod.mostrar_info())
            else:
                self._mostrar("Producto no encontrado")
        else:
            nom = simpledialog.askstring("Buscar", "Nombre del producto:")
            if not nom: return
            idx, prod = self._inventario.buscar_lineal_por_nombre(nom.strip())
            if prod:
                self._mostrar(f"Encontrado en posicion {idx}")
                self._mostrar(prod.mostrar_info())
            else:
                self._mostrar("Producto no encontrado")

    def _reg_proveedor(self):
        ruc = simpledialog.askstring("Proveedor", "RUC:")
        if not ruc: return
        nom = simpledialog.askstring("Proveedor", "Nombre:")
        if not nom: return
        tel = simpledialog.askstring("Proveedor", "Telefono:") or ""
        email = simpledialog.askstring("Proveedor", "Email:") or ""
        dirr = simpledialog.askstring("Proveedor", "Direccion:") or ""
        self._inventario.registrar_proveedor(Proveedor(ruc, nom, tel, email, dirr))
        self._mostrar(f"OK Proveedor registrado: {nom}")

    def _movimiento(self):
        cod = simpledialog.askstring("Movimiento", "Codigo del producto:")
        if not cod: return
        prod = self._inventario.buscar_producto(cod.strip())
        if not prod:
            self._mostrar("Producto no encontrado")
            return
        try:
            cant = int(simpledialog.askstring("Movimiento", "Cantidad:") or 0)
        except:
            return
        tipo = simpledialog.askstring("Movimiento", "Tipo (entrada/salida):")
        if not tipo: return
        if tipo.lower() == "entrada":
            mov = Entrada(prod, cant)
            self._inventario.entrada_mercancia(mov)
        else:
            mov = Salida(prod, cant)
            self._inventario.salida_mercancia(mov)
        self._mostrar(f"OK {mov.resumen()} | Stock: {prod.stock_actual}")

    def _deshacer(self):
        mov = self._inventario.deshacer_movimiento()
        if mov:
            self._mostrar(f"OK Deshecho: {mov.resumen()}")
        else:
            self._mostrar("No hay movimientos para deshacer")

    def _pedido(self):
        self._contador_pedidos += 1
        cli = simpledialog.askstring("Pedido", "Cliente:") or "Cliente"
        pedido = Pedido(self._contador_pedidos, cli)
        while True:
            cod = simpledialog.askstring("Pedido", "Codigo de producto (vacio = terminar):")
            if not cod: break
            prod = self._inventario.buscar_producto(cod.strip())
            if prod:
                cant = int(simpledialog.askstring("Pedido", "Cantidad:") or 1)
                pedido.agregar_producto(prod, cant)
                self._mostrar(f"  -> {prod.nombre} x{cant}")
            else:
                self._mostrar("  Producto no encontrado")
        self._inventario.agregar_pedido(pedido)
        self._mostrar(f"OK Pedido #{pedido.id_pedido} agregado - Total: ${pedido.calcular_total():.2f}")

    def _procesar_pedido(self):
        pedido = self._inventario.procesar_pedido()
        if pedido:
            self._mostrar(f"OK Procesado:\n{pedido.mostrar_info()}")
        else:
            self._mostrar("No hay pedidos pendientes")

    def _bajo_stock(self):
        bajos = self._inventario.reporte_bajo_stock()
        self._mostrar("=== BAJO STOCK ===")
        if not bajos:
            self._mostrar("Todos los productos tienen stock suficiente")
        for p in bajos:
            self._mostrar(p.mostrar_info())

    def ejecutar(self):
        self._ventana.mainloop()
