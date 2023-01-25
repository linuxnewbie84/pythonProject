class Punto2d:
    def __init__(self, x, y):
        self.x  = x
        self.y = y

    def traslacion(self, a, b):
        self.x += a
        self.y += b
    def __str__(self):
        return "x: {}; Y:{}".format(self.x, self.y)

class Punto3d(Punto2d):
    def __init__(self,x,y,z):
        #Inicilazación de las coordenadas x e y y del punto, usando
        #El constructor de Punto2d, aquí no hay acceso directo
        super().__init__(x,y)
    #Inicialización de la coordenada z
        self.z = z
    def traslacion(self, x,y,z):
        super().__init__(self,x, y)
        self.z += z
    def __str__(self):
        _2d = super().__str__()
        return "{}; Z= {}".format(_d, self.z)

b = Punto2d(5,6)
b.traslacion(2, -2)
c = Punto3d(5,6,7)
c.traslacion(3,2,3)
