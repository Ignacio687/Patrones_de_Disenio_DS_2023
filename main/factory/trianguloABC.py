from abc import ABCMeta, abstractmethod
from main.product import TrianguloObjectABC

class TrianguloABC(metaclass = ABCMeta):

    @abstractmethod
    def createTriangulo(self, ladoA: int, ladoB: int, ladoC: int) -> TrianguloObjectABC:
        pass
