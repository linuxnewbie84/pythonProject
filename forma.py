""Clase Base"""
class Forma:
    """El método polimófico, que seá especializado para cada clase derivada"""
    def perimetro(self):
        raise NotImplementedError("Imposible calcular el perímetro")

class Circulo(Forma):
    def __init__(self):
        super().__init__():