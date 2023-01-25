
from cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self,titular, cantidad, edad):
        super().__init__(titular, cantidad)
        self.__edad = edad
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, v):
        self.__edad = v
    def esvalido(self):
        if self.__edad >= 18 and self.__edad <= 25:
            return 1
    def mostrar(self):
        print("El titular {}, tiene de fondos {} y es una cuenta Joven".format(self.titular, self.cantidad))
c2 = CuentaJoven("Sandra",2500, 25)
c2.esvalido()
c2.mostrar()
if c2.esvalido() == True:
    r = int(input("Ingrese la cantidad que de desea retirar"))
    c2.retirar = r
c2.mostrar()
