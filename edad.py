class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def calcularaño(self):
        self.edad = self.edad - 2022
        return self.edad

    def mostrar(self):
        print("{} eres del año {}".format(self.nombre, self.edad))


p = Persona("Alberto", 39)
p.calcularaño()
p.mostrar()