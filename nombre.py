class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular(self):
        l = 0
        for i in self.nombre:
            if i.lower() in "aeiou":
                l +=1
        print("El total de vocales que conforman tu nombre es: {}".format(l))
p = Persona("Alberto")
p.calcular()