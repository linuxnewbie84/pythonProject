#Primera clase
class Druida:
    def __init__(self):
        self.magia = 4
#Segunda Clase

class Ladron:
    def __init__(self):
        self.habilidad = 7
#Una clase derivada

class Heroes(Ladron, Druida): #Clase que hereda de dos clases
    pass

h = Heroes()
#Imprimirá un valor booleano si es una instancia de la clase Ladron
print(isinstance(h, Ladron))
#Imprimirá un valor booleano si es una instancia de la clase Druida
print(isinstance(h, Druida))