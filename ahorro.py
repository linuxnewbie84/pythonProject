class Cuenta:
    def __init__(self, titular, monto):
        self.__titular = titular
        self.__monto = monto
    def mostra(self):
        print("El titual de la cuenta{} , tiene un  monto de ${}".format(self.__titular, self.__monto))

    @property
    def titular(self):
        return self.__titular
    @property
    def monto(self):
        return self.__monto
    @monto.setter
    def ingresar(self, deposito):
        self.__monto = self.__monto + deposito

    @monto.setter
    def retirar(self, retiro):
        if retiro > self.__monto:
            print("No se cuenta con saldo suficiente")
        else:
            self.__monto = self.__monto - retiro
            