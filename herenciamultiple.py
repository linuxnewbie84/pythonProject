#implementar un programa que calcule la superficie total de una casa, sabiendo que una casa está formada por
#paredes y que cada pared tiene una orientación (Norte, oeste, sur, este) y posiblemente ventanas. Una ventana tiene
#una superficie que se da como párametro durante la construcción
#
class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        "Una pared no tiene ninguna ventada por defecto"
        self.ventana = []

class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        "Se añade la ventana a la pared dada como argumento"
        self.pared.ventana.append(self)

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def sueprficie_cristales(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventana:
                superficie += ventana.superficie
        return superficie

