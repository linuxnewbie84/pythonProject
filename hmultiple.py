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
#atributos recuperados de Herencia
print(h.magia)
#Provoca un error porque no ha sido bien definidad
#La habilidad sí está bien definida, ésto porque la clase Ladron se situó en primer lugar
print(h.habilidad)

