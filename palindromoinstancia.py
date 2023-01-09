#Palíndromo método instancia
#En la clase palíndromo añada un atributo que se incializará en el constructor, Añada también un metodo test() que com
#pruebe si el atributo de la instancia es palíndromo. Además, al destruir la instancia, muesrre el atributo en mayúscula

class Palindromo:
    def __init__(self, cadena):
        self.cadena = cadena
    def __del__(self):
        print(self.cadena.upper()) #El Recolector de basura destruye y manda en mayusculas la palabra radar
    def test(self):
        return Palindromo.esPalindromo(self.cadena)
    def esPalindromo(s):
    #una cadena de único caracater o una cadena vacía son palindromos
        if len(s) <=1:
            return True
        #Si el primer y último carácter son iguales, y si la subcadena restante es ella misma
        #un palíndromo, entonces toda la cadena es un palíndromo

        #El uso del índice -1 permite recuperar el último carácter de una cadena
        #El uso del carácter ':' permite extraer una subcadena que especifica los índices de inicio y fin.
        return s[0]== s[-1]and Palindromo.esPalindromo(s[1:-1])
a = Palindromo("radar")
print(a.test())