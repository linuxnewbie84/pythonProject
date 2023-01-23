from ahorro import Cuenta

class CajadeAhorro(Cuenta):
    def __init__(self, titular, monto):
        super().__init__(titular, monto)
    def mostrar(self):
        print("Los datos de la cuenta son:\n")
        super().mostra()
class PlazoFijo(Cuenta):
    def __init__(self, titular, monto, plazo, interes):
        super().__init__(titular, monto)
        self.plazo = plazo
        self.interes = interes

    def imprimir(self):
        print("Cuenta de plazo fijo")
        super().mostra()
        print("Plazo en dias:", self.plazo)
        print("Interes:", self.interes)
        self.ganancia_interes()

    def ganancia_interes(self):
        ganancia = self.monto * self.interes / 100
        print(ganancia)

c = CajadeAhorro("Jesus Alberto Palma García", 2000)
c.mostrar()
p = PlazoFijo("Jesús Alberto Palma García", 3000, 30, 10)
p.imprimir()