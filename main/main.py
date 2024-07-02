from main.factory import FactoryLcdBlue, FactoryPlasmaYellow, TVFactoryABC
from main.product import TV, LCD, plasma

class Cliente():
    def __init__(self, factory: TVFactoryABC) -> None:
        self.factory = factory

    def run(self):
        self.factory.assemble()
        
class ClienteConfig():
    def main(self) -> Cliente:
        while True:
            tvTipe = input("Seleccione una opcion(escriba el número correspondiente):"
                           + "\n1 - LCD\n2 - plasma\n").strip()
            if tvTipe == "1":
                return Cliente(FactoryLcdBlue())
            elif tvTipe == "2":
                return Cliente(FactoryPlasmaYellow())