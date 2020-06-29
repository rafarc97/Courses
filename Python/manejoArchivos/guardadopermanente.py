import pickle

class Persona:
    def __init__(self, nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)
    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)


class ListaPersonas:

    personas=[]

    def __init__(self):
        listaDePersonas=open("../ficheroExterno", "ab+") #append binary
        listaDePersonas.seek(0) #colocamos puntero al inicio del fichero
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo" .format(len(self.personas)))
        except: #si no se pueden cargar datos (por ej. la 1ª vez que accedemos al fichero)
            print("EL fichero está vacío")
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()
    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas=open("../ficheroExterno", "wb") #write bytes
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)
    def mostrarInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()

p=Persona("Rafa","Masculino",23)
miLista.agregarPersonas(p)

p2=Persona("Amanda","Femenino",21)
miLista.agregarPersonas(p2)

p3=Persona("Fran","Masculino",30)
miLista.agregarPersonas(p3)

miLista.mostrarInfoFicheroExterno()
