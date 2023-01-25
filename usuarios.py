class User:
    def __init__(self, nombre, mail):
        self.__nombre = nombre
        self.__mail = mail

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, n):
        self.__nombre = n
    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def main(self,m):
        self.__mail = m


class Empleado(User):
    def __init__(self, nombre, mail, nempleado):
        super().__init__(nombre, mail)
        self.nempleado = nempleado
    def horas(self, horas):
        self.horas = horas
        if self.horas >=8:
            print("Usted es un Empleado completo con horas de trabajo asignadas{}".format(self.horas))

class Jefe(User):
    def __init__(self, nombre, mail, depto):
        super().__init__(nombre, mail)
        self.depto = depto


j = Empleado("betito", "rebeto@gmail.com", "2815")
print(j.nombre, j.mail, j.nempleado)
j.nombre = "roro"
print(j.nombre, j.mail, j.nempleado)
j.mail ="rebeto"