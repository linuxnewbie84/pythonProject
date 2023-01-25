class Jugador:
    inicio = 30
    def __init__(self, nombre, puntaje):
        self.nombre = nombre
        self.puntaje = puntaje

    def imprimir(self):
        print("El nombre del jugador es: {}, con un puntaje de: {} ".format(self.nombre, self.puntaje))
        print(Jugador.inicio)

    def tiempo(self):
        Jugador.inicio = Jugador.inicio -1

j = Jugador("Alberto", 56)
j.imprimir()
while j.inicio > 0:
    j.tiempo()
    j.imprimir()

