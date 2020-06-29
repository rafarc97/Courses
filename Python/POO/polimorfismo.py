class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


miVehiculo=Moto()
miVehiculo.desplazamiento()
miVehiculo2=Coche()
miVehiculo2.desplazamiento()
miVehiculo3=Camion()
miVehiculo3.desplazamiento()


#gracias al polimorfismo, el objeto vehiculo en función del contexto sabrá
#a que método desplazamineto llamar de los 3 existentes
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo4=Camion()
desplazamientoVehiculo(miVehiculo4)

#en este ejemplo como miVehiculo es un objeto de la clase Camion, al pasarlo
#por parámetros a dicha función e, polimorfismo haría que el objeto vehículo
#de la funcion desplazamientoVehiculo se transforme en un objeto de la clase
#camión y llamará a la función desplazamiento de la clase Camión.