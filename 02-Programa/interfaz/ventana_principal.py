import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from clases.producto import Producto, ProductoPerecedero, ProductoNoPerecedero
from clases.proveedor import Proveedor
from clases.movimiento import Entrada, Salida
from clases.pedido import Pedido


class VentanaPrincipal:
    def __init__(self, inventario):
        self._inventario = inventario
        self._contador_pedidos = 0
        self._ventana = tk.Tk()
        self._ventana.title("Inventario y Bodega - Grupo 7")
        self._ventana.geometry("750x500")
        self._configurar()

    def _configurar(self):
        marco = tk.Frame(self._ventana)
        marco.pack(pady=10)

        botones = [
            ("Registrar Producto", self._reg_producto),
            ("Listar Productos", self._listar),
            ("Eliminar Producto", self._eliminar_producto),
            ("Buscar por código", self._buscar),
            ("Registrar Proveedor", self._reg_proveedor),
            ("Listar Proveedores", self._listar_proveedores),
            ("Eliminar Proveedor", self._eliminar_proveedor),
            ("Entrada/Salida", self._movimiento),
            ("Deshacer", self._deshacer),
            ("Ver Movimientos", self._ver_movimientos),
            ("Nuevo Pedido", self._pedido),
            ("Procesar Pedido", self._procesar_pedido),
            ("Bajo Stock", self._bajo_stock),
            ("Rotar Inventario", self._rotar),
            ("Ord. Burbuja", self._ord_burbuja),
            ("Ord. Merge Sort", self._ord_merge),
            ("Búsq. Lineal", self._busq_lineal),
            ("Búsq. Binaria", self._busq_binaria),
        ]

        fila = 0
        col = 0
        for texto, comando in botones:
            tk.Button(marco, text=texto, width=18, command=comando).grid(row=fila, column=col, padx=3, pady=3)
            col += 1
            if col == 4:
                col = 0
                fila += 1

        self._output = scrolledtext.ScrolledText(self._ventana, height=20, font=("Consolas", 10))
        self._output.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        tk.Button(self._ventana, text="Salir", command=self._ventana.quit).pack(pady=5)

    def _mostrar(self, texto):
        self._output.insert(tk.END, texto + "\n")
        self._output.see(tk.END)

    def _reg_producto(self):
        cod = simpledialog.askstring("Producto", "Código:")
        if not cod: return
        nom = simpledialog.askstring("Producto", "Nombre:")
        if not nom: return
        cat = simpledialog.askstring("Producto", "Categoría:") or ""
        try:
            pre = float(simpledialog.askstring("Producto", "Precio:") or 0)
            stock = int(simpledialog.askstring("Producto", "Stock actual:") or 0)
            smin = int(simpledialog.askstring("Producto", "Stock mínimo (0):") or 0)
            smax = int(simpledialog.askstring("Producto", "Stock máximo (999):") or 999)
        except:
            messagebox.showerror("Error", "Valores numéricos inválidos")
            return

        self._inventario.registrar_producto(Producto(cod, nom, cat, pre, stock, smin, smax))
        self._mostrar(f"✓ Producto registrado: {cod} - {nom}")

    def _listar(self):
        prods = self._inventario.listar_productos()
        self._mostrar("=== PRODUCTOS ===")
        if not prods:
            self._mostrar("(vacío)")
        for p in prods:
            self._mostrar(p.mostrar_info())

    def _buscar(self):
        cod = simpledialog.askstring("Buscar", "Código:")
        if not cod: return
        p = self._inventario.buscar_producto(cod.strip())
        if p:
            self._mostrar(p.mostrar_info())
        else:
            self._mostrar("Producto no encontrado")

    def _reg_proveedor(self):
        ruc = simpledialog.askstring("Proveedor", "RUC:")
        if not ruc: return
        nom = simpledialog.askstring("Proveedor", "Nombre:")
        if not nom: return
        tel = simpledialog.askstring("Proveedor", "Teléfono:") or ""
        email = simpledialog.askstring("Proveedor", "Email:") or ""
        dirr = simpledialog.askstring("Proveedor", "Dirección:") or ""
        self._inventario.registrar_proveedor(Proveedor(ruc, nom, tel, email, dirr))
        self._mostrar(f"✓ Proveedor registrado: {nom}")

    def _movimiento(self):
        cod = simpledialog.askstring("Movimiento", "Código del producto:")
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
        self._mostrar(f"✓ {mov.resumen()} | Stock: {prod.stock_actual}")

    def _deshacer(self):
        mov = self._inventario.deshacer_movimiento()
        if mov:
            self._mostrar(f"✓ Deshecho: {mov.resumen()}")
        else:
            self._mostrar("No hay movimientos para deshacer")

    def _pedido(self):
        self._contador_pedidos += 1
        cli = simpledialog.askstring("Pedido", "Cliente:") or "Cliente"
        pedido = Pedido(self._contador_pedidos, cli)
        while True:
            cod = simpledialog.askstring("Pedido", "Código de producto (vacío = terminar):")
            if not cod: break
            prod = self._inventario.buscar_producto(cod.strip())
            if prod:
                cant = int(simpledialog.askstring("Pedido", "Cantidad:") or 1)
                pedido.agregar_producto(prod, cant)
                self._mostrar(f"  → {prod.nombre} x{cant}")
            else:
                self._mostrar("  Producto no encontrado")
        self._inventario.agregar_pedido(pedido)
        self._mostrar(f"✓ Pedido #{pedido.id_pedido} agregado - Total: ${pedido.calcular_total():.2f}")

    def _procesar_pedido(self):
        pedido = self._inventario.procesar_pedido()
        if pedido:
            self._mostrar(f"✓ Procesado:\n{pedido.mostrar_info()}")
        else:
            self._mostrar("No hay pedidos pendientes")

    def _bajo_stock(self):
        bajos = self._inventario.reporte_bajo_stock()
        self._mostrar("=== BAJO STOCK ===")
        if not bajos:
            self._mostrar("Todos los productos tienen stock suficiente")
        for p in bajos:
            self._mostrar(p.mostrar_info())

    def _ord_burbuja(self):
        criterio = simpledialog.askstring("Ordenar", "Criterio (codigo/nombre/precio/stock):") or "codigo"
        prods = self._inventario.ordenar_burbuja(criterio.strip().lower())
        self._mostrar(f"=== ORDENADO POR {criterio} (Burbuja O(n²)) ===")
        for p in prods:
            self._mostrar(p.mostrar_info())

    def _ord_merge(self):
        criterio = simpledialog.askstring("Ordenar", "Criterio (codigo/nombre/precio/stock):") or "codigo"
        prods = self._inventario.ordenar_merge(criterio.strip().lower())
        self._mostrar(f"=== ORDENADO POR {criterio} (Merge Sort O(n log n)) ===")
        for p in prods:
            self._mostrar(p.mostrar_info())

    def _busq_binaria(self):
        cod = simpledialog.askstring("Búsqueda Binaria", "Código del producto:")
        if not cod: return
        idx, prod = self._inventario.buscar_binaria_por_codigo(cod.strip())
        if prod:
            self._mostrar(f"✓ Búsqueda binaria: encontrado en posición {idx}")
            self._mostrar(prod.mostrar_info())
        else:
            self._mostrar("Producto no encontrado")

    def _eliminar_producto(self):
        cod = simpledialog.askstring("Eliminar", "Código del producto:")
        if not cod: return
        prod = self._inventario.eliminar_producto(cod.strip())
        if prod:
            self._mostrar(f"✓ Producto eliminado: {prod.nombre}")
        else:
            self._mostrar("Producto no encontrado")

    def _listar_proveedores(self):
        provs = self._inventario.listar_proveedores()
        self._mostrar("=== PROVEEDORES ===")
        if not provs:
            self._mostrar("(vacío)")
        for p in provs:
            self._mostrar(p.mostrar_info())

    def _eliminar_proveedor(self):
        ruc = simpledialog.askstring("Eliminar Proveedor", "RUC:")
        if not ruc: return
        if self._inventario.eliminar_proveedor(ruc.strip()):
            self._mostrar(f"✓ Proveedor eliminado")
        else:
            self._mostrar("Proveedor no encontrado")

    def _ver_movimientos(self):
        movs = self._inventario.listar_movimientos()
        self._mostrar("=== HISTORIAL DE MOVIMIENTOS ===")
        if not movs:
            self._mostrar("(vacío)")
        for m in movs:
            self._mostrar(m.resumen())

    def _rotar(self):
        self._inventario.rotar_inventario()
        self._mostrar("✓ Inventario rotado (el primer producto ahora es el último)")

    def _busq_lineal(self):
        nom = simpledialog.askstring("Búsqueda Lineal", "Nombre del producto:")
        if not nom: return
        idx, prod = self._inventario.buscar_lineal_por_nombre(nom.strip())
        if prod:
            self._mostrar(f"✓ Búsqueda lineal: encontrado en posición {idx}")
            self._mostrar(prod.mostrar_info())
        else:
            self._mostrar("Producto no encontrado")

    def ejecutar(self):
        self._ventana.mainloop()
