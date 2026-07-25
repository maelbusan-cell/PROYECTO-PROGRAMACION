from abc import ABC, abstractmethod

class Registrable(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass
