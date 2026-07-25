from .registrable import Registrable


class Proveedor(Registrable):
    def __init__(self, ruc, nombre, telefono, email, direccion):
        self._ruc = ruc
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._direccion = direccion

    @property
    def ruc(self):
        return self._ruc

    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono

    @property
    def email(self):
        return self._email

    @property
    def direccion(self):
        return self._direccion

    def mostrar_info(self):
        return (f"[{self._ruc}] {self._nombre} | "
                f"Tel: {self._telefono} | {self._email}")
