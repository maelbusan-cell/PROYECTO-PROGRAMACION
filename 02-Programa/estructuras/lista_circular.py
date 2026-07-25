from .nodo import Nodo


class ListaCircular:
    def __init__(self):
        self._ultimo = None
        self._tamano = 0

    @property
    def ultimo(self):
        return self._ultimo

    @property
    def tamano(self):
        return self._tamano

    def esta_vacia(self):
        return self._ultimo is None

    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.esta_vacia():
            nuevo.siguiente = nuevo
            nuevo.anterior = nuevo
            self._ultimo = nuevo
        else:
            primero = self._ultimo.siguiente
            nuevo.siguiente = primero
            nuevo.anterior = self._ultimo
            primero.anterior = nuevo
            self._ultimo.siguiente = nuevo
        self._tamano += 1

    def eliminar(self, codigo):
        if self.esta_vacia():
            return None
        actual = self._ultimo.siguiente
        for _ in range(self._tamano):
            if actual.dato.codigo == codigo:
                if self._tamano == 1:
                    self._ultimo = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    if actual == self._ultimo:
                        self._ultimo = actual.anterior
                self._tamano -= 1
                return actual.dato
            actual = actual.siguiente
        return None

    def buscar(self, codigo):
        if self.esta_vacia():
            return None
        actual = self._ultimo.siguiente
        for _ in range(self._tamano):
            if actual.dato.codigo == codigo:
                return actual.dato
            actual = actual.siguiente
        return None

    def recorrer(self):
        if self.esta_vacia():
            return []
        resultado = []
        actual = self._ultimo.siguiente
        for _ in range(self._tamano):
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado

    def rotar(self):
        if self._ultimo is not None:
            self._ultimo = self._ultimo.siguiente
