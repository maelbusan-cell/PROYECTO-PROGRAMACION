from .nodo import Nodo


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
