from datetime import datetime


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
