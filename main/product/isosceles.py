from . import TrianguloObjectABC

class Isosceles(TrianguloObjectABC):

    def getDescripcion(self) -> str:
        return "Es un triangulo Isosceles"

    def getSuperficie(self, base: float, altura: float) -> float:
        return base * altura

    def dibujate(self) -> None:
        pass