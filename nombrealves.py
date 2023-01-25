class Nombre:
    def __init__(self, nombre):
        self.nombre = nombre
    def alreve(self):
        for i in range(len(self.nombre), 0, -1):
            print(self.nombre[i-1])

p = Nombre("Alberto")
p.alreve()