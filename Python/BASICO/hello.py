#Primer "Hola Rafa"
print("hello rafa")

#Práctica desaconsejada -> MÁS de UNA instruc. en una línea
print("hello rafa") ; print("We are learning about Python")

#Dividir una misma instruc. en varias líneas usando "\":
my_name="my name \
is rafa"



#Tipos datos

#Numéricos: int, float y complejos
#Textos: han de ir entre comillas (triples, dobles o simples)
#Booleanos: True y false


#Operadores

#Aritméticos: + suma, - resta, * multiplicación, / división, % módulo, ** exponente, // div. entera
#Comparación: == igual que, != diferente que, > mayor que, < menor que, >= mayor/igual que, <= menor/igual que
#Lógicos: AND, OR y NOT
#Asignación: = igual, += incremento, -= decremento, *=, , /=, %=, **=, //=
#Especiales: IS, IS NO, IN, NOT IN


#Variables:

#Solo pueden tener letras mayúsculas, minúsculas, números y "_"
#El tipo de variable lo establece el contenedor
#Python es un lenguaje 100% orientado a objetos
#Cuando creamos una variable p. ej número=5, esta sería un objeto

#La función type() nos devuelve el tipo de variable con la nomenclatura class
nombre=5
print(type(nombre)) #nos devuelve class 'int'

#Para imprimir mensajes con 3 saltos de línea usamos las triples comillas
mensaje="""Esto es un mensaje
con tres saltos
de línea"""
print(mensaje)



#Funciones o Métodos (si están definidas en una clase):
#Python pasa todo por referencias a diferencia de otros lenguajes
def mensaje():
    print("Mensaje impreso dentro de una función")
    print("Mensaje impreso dentro de una función")
    print("Mensaje impreso dentro de una función")

mensaje()

#Transformaciones mayúsculas/minúsculas

palabra=input("Introduce una palabra en mayuscula: ")
transformamayuscula=palabra.lower()
print(transformamayuscula)

palabra2=input("Introduce una palabra en minuscula: ")
transformaminuscula=palabra.upper()
print(transformaminuscula)




#ESTRUCTURAS DE DATOS:

#-LISTAS
#-TUPLAS
#-DICCIONARIOS