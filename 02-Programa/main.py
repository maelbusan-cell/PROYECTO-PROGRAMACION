from clases.inventario import Inventario
from interfaz.ventana_principal import VentanaPrincipal
from base_datos.conexion import ConexionDB


def main():
    db = ConexionDB()
    db.conectar()
    db.crear_tablas()
    inventario = Inventario(db=db)
    app = VentanaPrincipal(inventario)
    app.ejecutar()
    db.desconectar()


if __name__ == "__main__":
    main()
