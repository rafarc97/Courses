class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario


    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleados=[
    Empleado("Juan", "Direccion", 6700),
    Empleado("Ana", "Presidenta", 7500),
    Empleado("Rafa", "Administrativo", 2100),
    Empleado("Sara", "Secretaria", 2150),
    Empleado("Mario", "Botones", 1800),
]

def calculo_comision(empleado):
    #sumo al salario de cada empelado un 3%
    if empleado.salario < 3000:
        empleado.salario=empleado.salario*1.03
    return empleado

#aplica una funcion a cada elemento de una lista iterable (listas, tuplas,etc...)
#devolviendo una lista con los resultados
listaEmpleadosComision=map(calculo_comision,listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)