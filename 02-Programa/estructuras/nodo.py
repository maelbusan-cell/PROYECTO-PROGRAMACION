class Nodo:
    def __init__(self, dato):
        self._dato = dato
        self._siguiente = None
        self._anterior = None

    @property
    def dato(self):
        return self._dato

    @dato.setter
    def dato(self, valor):
        self._dato = valor

    @property
    def siguiente(self):
        return self._siguiente

    @siguiente.setter
    def siguiente(self, nodo):
        self._siguiente = nodo

    @property
    def anterior(self):
        return self._anterior

    @anterior.setter
    def anterior(self, nodo):
        self._anterior = nodo
