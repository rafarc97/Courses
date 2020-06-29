class Persona():
    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia
    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)


class Empleado(Persona):
    def __init__(self, salario,  antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        #con esto conseguimos que el
        #objeto Antonio tenga las propiedades nombre, edad y lugar_residencia
        #pertenecientes a la clase Persona.
        self.salario=salario
        self.antigüedad=antigüedad
    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "Antigüedad: ", self.antigüedad)


Manuel=Empleado(1500,15, "Manuel", 55, "Colombia")
Manuel.descripcion()


#PRINCIPIO DE SUSTITUCIÓN: un objeto de una subclase es siempre un objeto
#de una super clase, pero viceversa no. En nuestro ejemplo, un objeto de Persona
# es siempre un objeto de una Persona pero no viceversa.

#La función isinstance() nos dice si un objeto pertenece a una clase o no.
#Muy útil cuando trabajemos con programas los cuales utilicen muchas clases.

print(isinstance(Manuel,Persona)) #nos devuelve True
#si Manuel fuera una instancia de Persona y le hacemos el isinstance(Manuel,Empleado)
#nos devolvería False.