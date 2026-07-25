from .registrable import Registrable


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
