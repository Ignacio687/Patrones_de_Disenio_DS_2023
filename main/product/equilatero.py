from . import TrianguloObjectABC

class Equilatero(TrianguloObjectABC):

    def getDescripcion(self) -> str:
        return "Soy un triangulo Equilatero"

    def getSuperficie(self, base: float, altura: float) -> float:
        return base * altura

    def dibujate(self) -> None:
        pass