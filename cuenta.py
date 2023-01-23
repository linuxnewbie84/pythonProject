#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona)
# y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional.
# Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente,
# sólo ingresando o retirando dinero.
# mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class Cuenta:
    def __init__(self, titular, cantidad):
        self.__titular = titular
        self.__cantidad = cantidad

    def mostrar(self):
        print("El titular de la cuenta {0}, tiene un saldo de ${1}".format(self.__titular, self.__cantidad))
    @property
    def titular(self):
        return  self.__titular
    @titular.setter
    def titular(self,n):
        self.__titular = n
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def ingresar(self, can):
        if self.__cantidad > 0:
            self.__cantidad = self.__cantidad + can
        else:
            print("Ingrese un monto valido")
    @cantidad.setter
    def retirar(self, can):
        if can < self.__cantidad:
            self.__cantidad = self.__cantidad - can
        else:
            print("No se puede hacer el retiro, no cuenta con fondos disponibles")

p1 = Cuenta("Alberto", 2000)
p1.mostrar()
print(p1.titular)
print(p1.cantidad)
p1.ingresar = 2000
p1.mostrar()
p1.retirar = 500
p1.mostrar()