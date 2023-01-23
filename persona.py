#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#mostrar(): Muestra los datos de la persona.
#esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    #Propertyś
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    #Getter normal
    def get_dni(self):
        return self.__dni
    @nombre.setter
    def nombre(self, nnom):
        self.__nombre = nnom
    @edad.setter
    def edad(self, valor):
        self.__edad = valor
    def set_dni(self, dn):
        self.__dni = dn
prueba = Persona('Alberto', 38, 457136)
print(prueba)
print(prueba.edad)
print(prueba.get_dni())
print(prueba.nombre)
prueba.set_dni(78945)
prueba.nombre = 'Mario'
prueba.edad = 85
print(prueba.edad)
print(prueba.get_dni())
print(prueba.nombre)
