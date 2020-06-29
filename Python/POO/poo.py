#Programacion orientada a objetos

#SELF: hace referencia a el propio objeto perteneciente a la clase, a la
#instancia perteneciente a la clase

#PASS: por si no hemos aun creado dicho metodo y no queremos que nos de
#fallo al ejecutar el programa se pone pass.

#CONSTRUCTOR: forma de especificar claramente cual será el estado inicial de los
#objetos creados de una clase. Para ello definimos un metodo __init__(self).

#ENCAPSULACIÓN: proteger una propiedad de la clase para que no se pueda modificar
#desde fuera de la clase. se pueden encapsular metodos y/ variables de la clase
#las variables y/o metodos encapsulados solo podran ser modificados por metodos
#que estén dentro de la propia clase.

#debemos encapsular nuestras variables/metodos cuando mi clase lo necesite y
#eso depende del comportamiento que quiero que tenga dicha clase, bajo mi criterio

#EJEMPLO:

class Coche():

    def __init__(self): #método constructor
        self.__largoChasis=250 #variable encapsulada
        self.__anchoChasis=120 #variable encapsulada
        self.__ruedas=4 #variable encapsulada
        self.__enmarcha=False #variable encapsulada

    def arrancar(self, arrancamos): #self = la instancia "miCoche"
        #pass
        self.__enmarcha=arrancamos

        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()
        if(self.__enmarcha and chequeo):
             return "EL coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
             return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas, un ancho de ",
              self.__anchoChasis, "y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("realizando chequeo interno")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche=Coche() #crear un objeto (instanciar/ejemplarizar un clase)
print(miCoche.arrancar(True))
miCoche.estado()

miCoche2=Coche() #crear un objeto (instanciar/ejemplarizar un clase)
print(miCoche.arrancar(False))
miCoche2.__ruedas = 2 #no se realiza por estar encapsulada la variable __ruedas
miCoche2.estado()
print(miCoche2.__chequeo_interno()) # nos da un mensaje de error por estar encapsulado
#el metodo al que estamos llamando.

