from main.director import AutoDirector
from main.builder import FiatBuilder, FordBuilder, AutoBuilderABC

class Client():

    def __init__(self) -> None:
        self.director = AutoDirector()
        self.autoFordBuilder: AutoBuilderABC = FordBuilder()
        self.autoFiatBuilder: AutoBuilderABC = FiatBuilder()

    def run(self) -> None:
        for constructor in [self.autoFordBuilder, self.autoFiatBuilder]:
            self.director.builder = constructor
            print(f"Construyendo auto")
            self.director.constructAuto()
            auto = self.director.builder.product
            print(f"Marca: {auto.getMarca()}")
            print(f"Modelo: {auto.getModelo()}\n")
        ##Construcción personalizada
        self.autoFordBuilder.reset()
        print(f"Construyendo auto sin modelo")
        self.autoFordBuilder.buildMarca()
        self.autoFordBuilder.buildMotor()
        auto = self.autoFordBuilder.product
        print(f"Marca: {auto.getMarca()}")
        print(f"Modelo: {auto.getModelo()}\n")