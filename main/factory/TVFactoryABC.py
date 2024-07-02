from abc import ABCMeta, abstractmethod
from . import TVFactoryABC
from main.product import Color, TV

class TVFactoryABC(metaclass=ABCMeta):

    @abstractmethod
    def createTV(self) -> TV:
        pass

    @abstractmethod
    def createColor(self, color: Color) -> Color:
        pass

    @abstractmethod
    def showTVdetails(self, tv: TV) -> None:
        pass

    def assemble(self) -> TV:
        color = self.createColor()
        print("Color TV: "+color.getDescription())
        tv = self.createTV(color)
        print(f"Fabricando {tv.getDescription()}")
        self.showTVdetails(tv)
        return tv
