# forma parte de un grupo de funciones que se llaman de orden superior,
# usaremos programación funcional (otro paradgima que soporta python).

# comprueba que los elemtnos de una secuencia cumplen una condición
# devolviendo un iterador con los elementos que cumplen dicha condinción

'''
def numero_par(num):
    if num%2==0:
        return True

numeros = [17,24,7,39,8,51,92]

#nos devuelve en formato objeto los numeros que cumplen lo que devuelve la funcion
#le ponemos list para que lo transforme a formato lsita  y podamos imprimirlo
print(list(filter(numero_par,numeros)))
'''

# todo esto se puede hacer usando lambda también, conseguimos mucha potencia:
'''
numeros=[17,24,7,39,8,51,92]
print(list(filter(lambda numero_par: numero_par%2==0, numeros)))
'''




class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario


    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)


listaEmpleados=[
    Empleado("Juan", "Direccion", 750000),
    Empleado("Ana", "Presidenta", 850000),
    Empleado("Rafa", "Administrativo", 250000),
    Empleado("Sara", "Secretaria", 270000),
    Empleado("Mario", "Botones", 210000),
]

    salarios_altos=filter(lambda empleado:empleado.salario>50000,listaEmpleados)

    for empleado_salario in salarios_altos:
        print(empleado_salario)
