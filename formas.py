from forma import Forma

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    #Sobrecarga del método de base
    def perimetro(self):
        return 4 * self.lado
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        #Una nueva sobrecarga del método de base

        def perimetro(self):
            return  2 * 3.1416 * self.radio
#Creación de una lista de formas concretas
formas_c =[Circulo(3),Cuadrado(5), Circulo(6)]

