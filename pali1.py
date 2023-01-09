#Palíndromo crear una clase palindromo que contenga un metodo de clase esPalindromo que devuelva un booleano
#que indica si una cadena de caracteres es un palíndromo
#comportamiento esperado: print(Palidromo.esPalidromo('radar'))
#>>True
#Solución

class Palindromo:
    #Metodo clase que verifica si la cadena "s" es un palíndromo
    def esPalindromo(s):
    #una cadena de único caracater o una cadena vacía son palindromos
        if len(s) <=1:
            return True
        #Si el primer y último carácter son iguales, y si la subcadena restante es ella misma
        #un palíndromo, entonces toda la cadena es un palíndromo

        #El uso del índice -1 permite recuperar el último carácter de una cadena
        #El uso del carácter ':' permite extraer una subcadena que especifica los índices de inicio y fin.
        return s[0]== s[-1]and Palindromo.esPalindromo(s[1:-1])
print(Palindromo.esPalindromo('radar'))
print(Palindromo.esPalindromo('arde ya la yedra'))
print(Palindromo.esPalindromo('LOL'))