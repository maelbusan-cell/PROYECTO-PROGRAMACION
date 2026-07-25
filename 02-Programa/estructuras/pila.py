from .nodo import Nodo


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
