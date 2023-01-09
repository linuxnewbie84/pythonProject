#Definición de la clase base

class Forma:
    #Construcctor de la clase base
    def __init__(self):
        print("Init Forma")
        self.x = 0
        self.y = 0
#Definición de la clase derivada

class Circulo(Forma):
    #Construcctor de la Clase derivada
    def __init__(self):
        print("Init de Circulo")
        super().__init__()

c = Circulo()
print(c.x, c.y)
