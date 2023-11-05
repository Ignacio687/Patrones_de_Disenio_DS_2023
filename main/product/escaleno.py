from . import TrianguloObjectABC

class Escaleno(TrianguloObjectABC):

    def getDescripcion(self) -> str:
        return "Es un triangulo Escaleno"

    def getSuperficie(self, base: float, altura: float) -> float:
        return base * altura

    def dibujate(self) -> None:
        pass