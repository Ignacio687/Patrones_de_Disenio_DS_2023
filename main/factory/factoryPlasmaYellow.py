from . import TVFactoryABC
from main.product import Yellow, Plasma, Color, TV

class FactoryPlasmaYellow(TVFactoryABC):

    def createColor(self) -> Color:
        return Yellow()

    def createTV(self, color: Color) -> TV:
        return Plasma(brand="Samsung", inches=45, color=color, price=55000, visionAngle=175, responseTime=1)
    
    def showTVdetails(self, tv: TV) -> None:
        print(f"Angulo de vision: {tv.getVisionAngle()}")
        print(f"Tiempo de respuesta: {tv.getResponseTime()}")
