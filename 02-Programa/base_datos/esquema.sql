-- Abrir este archivo en DB Browser for SQLite y ejecutar
-- Database: inventario.db

CREATE TABLE proveedores (
    ruc TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    telefono TEXT,
    email TEXT,
    direccion TEXT
);

CREATE TABLE productos (
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
);

CREATE TABLE movimientos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT NOT NULL,
    codigo_producto TEXT NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    proveedor_ruc TEXT,
    destino TEXT,
    FOREIGN KEY (codigo_producto) REFERENCES productos(codigo),
    FOREIGN KEY (proveedor_ruc) REFERENCES proveedores(ruc)
);
