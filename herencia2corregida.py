#Declaración de la Clase Base
#Herencia Simple
class Forma:
    #Construcctor de la clase base
    def __init__(self):
        print("Init de Forma")
        #Incialización de los atributos
        self.x = 0
        self.y = 0
#Definición de la clase derivada
class Circulo(Forma):
    #Construcctor de la clase derivada
    def __init__(self):
        #Llamada al contrucctor de la clase base
        Forma.__init__(self)
        print("Init Circulo")
c = Circulo()
print(c.x, c.y)
