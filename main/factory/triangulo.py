from . import TrianguloFactoryABC
from main.product import TrianguloObjectABC, EquilateroObject, EscalenoObject, IsoscelesObject

class Triangulo(TrianguloFactoryABC):

    def createTriangulo(self, ladoA: int, ladoB: int, ladoC: int) -> TrianguloObjectABC:
        if (ladoA == ladoB) and (ladoB == ladoC) and (ladoA == ladoC):
            equilateroObject = EquilateroObject(ladoA,ladoB,ladoC)
            return equilateroObject
        else:
            if (ladoA!=ladoB) and (ladoB!=ladoC) and (ladoA!=ladoC):
               escalenoObject = EscalenoObject(ladoA,ladoB,ladoC)
               return escalenoObject
            else:
                isoscelesObject = IsoscelesObject(ladoA,ladoB,ladoC)
                return isoscelesObject