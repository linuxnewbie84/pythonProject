"""Definició de la Clase Base"""
class Forma:
    x = 0
    y = 0
"""Definición de la Clase derivada"""
class Circulo(Forma):
    """Cuerpo de la Clase"""
    pass
c = Circulo()
print(c.x,c.y)