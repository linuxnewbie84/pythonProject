#Escriba una clase logger cuyo objetivo sea escribir un mensaje dado comko parámetro en un archivo cada vez que se llame
#al método log(mensaje). La primer linea del archivo debe de ser "--Star log--", seguida de los mensajes recibidos por
#el método log en la parte superior de un mensaje por línea, y la última líne del archvio, escrita cuando se destruye la
#instancia de logger, debe ser "--End log: x log(s)-" donde x es el número de llamadas al método log. Esta clase Logger
#se utilizará es un método llamada() de una clase Test.

#comportamiento esperado:
#test = Test()
#for i in range(1,6):
#if i == 1:
    #test.llamada("Primera llamada")
    #else:
        #test.llamada("{} llamada".format(string))

class logger:
    def __init__(self):
        #Apertura del archivo en modo escritura
        self.log_file = open("log.txt", "w")
        #Inicialización del contador de logs
        self.log_count = 0
        #Escritura de la primera línea
        self.log_file.write("--Start log --\n")

    def __del__(self):
        #Destrucción de la instancia:
        #se escribe la última línea del archivo
        self.log_file.write("End log: {} log(s)--\n".format(self.log_count))
        #Cierre correcto del archivo
        self.log_file.close()
    def log(self,mensaje):
        #Escritura del mensaje que se pasa como argumento
        self.log_file.write("{}\n".format(mensaje))
class test:
    def __init__(self):
        self.logger = Logger()
    def llamada(self,mensaje):
        self.logger.log(mensaje)