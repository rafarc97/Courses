#

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena)


class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"


miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#clase moto que hereda de la clase vehiculos (todo incluido el constructor)
class Moto(Vehiculos):
    #pass
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,
              "\nEn Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera,
              "\nFrenando: ", self.frena, "\n", self.hcaballito)

miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado() #llamamos al metodo estado de la clase moto por haber dos
# que se llaman igual (el de la clase padre y el de la propia clase moto


class VElectricos(Vehiculos):
    def __init__(self, marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
    def cargarEnergia(self):
        self.cargando=True
    def estado(self):
        super().estado()
        print("Autonomía: ", self.autonomia)

#herencia múltiple
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

#se le da siempre preferencia a la primera clase que se le indique,
#es decir estaremos heredando el constructor de la clase VElectricos
#por lo tanto al crear la instancia no le pasaremos ningún parametro puesto
#que el constructor de VElectrica no recibe ningun parametro.
#hay otros lenguajes que no soporta herencia multiple
miBici=BicicletaElectrica("Orbea","Hj")
print(miBici.estado())
#¿como hacemos entonces para que una instancia de la clase BicicletaElectrica
#pueda tener propiedades de marca y modelo? con la funcion super()
