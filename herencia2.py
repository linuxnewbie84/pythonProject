"""Definición de Clase base"""


class Forma:
    #Construcctor de la Clase
    def __init__(self):
        print("Init de la Forma")
        #Inicialización de los atributos
        self.x = 0
        self.y = 0

#Definición de las Clase derivada
class Circulo:
    #Constructor de la clase derivada, que no llama
    #al contrucctor de la clase base
    def __init__(self):
        print("Init de Circulo")

c = Circulo()

print(c.x, c.y)

#Dará un error por no llamar al construcctor de la clase base, y el error
#mencionará que los atributos x y y, no son parte del objeto clase
