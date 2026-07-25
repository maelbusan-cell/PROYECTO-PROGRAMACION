import sqlite3
import os


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
