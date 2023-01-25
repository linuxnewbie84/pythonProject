class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.__nota = nota
    def mostrar(self):
        print("El alumno {0}, tiene una calificación de {1}".format(self.nombre, self.__nota))
    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def recalificar(self, nota):
        self.__nota = nota

a = Alumno("Jesus Alberto Palma", 6)
a.mostrar()
if a.nota > 7:
    print("El alumno ha aprobado el curso")
else:
    print("se requiere una nota más alta")
    nota = int(input("Ingresa la nota:\n"))
    a.recalificar = nota
    a.mostrar()
