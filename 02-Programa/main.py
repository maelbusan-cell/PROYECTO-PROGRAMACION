from interfaz import VentanaPrincipal, Inventario, ConexionDB


def main():
    db = ConexionDB()
    db.conectar()
    db.crear_tablas()
    inv = Inventario(db=db)
    app = VentanaPrincipal(inv)
    app.ejecutar()
    db.desconectar()


if __name__ == "__main__":
    main()
