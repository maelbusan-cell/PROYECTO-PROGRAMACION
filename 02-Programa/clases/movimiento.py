from abc import ABC, abstractmethod
from datetime import datetime


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

    @property
    def aplicado(self):
        return self._aplicado

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
