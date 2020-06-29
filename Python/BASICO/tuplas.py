#Tuplas: son listas pero inmutables, no se pueden modificar

#se pueden extraer porciones creándose una nueva tupla
#Son + rápidas que las listas a la hora de ejecutarse debido a que ocupan
#menos espacio en memoria (están más optimizadas y por ello proporcionan un
#mayor rendimiento)
#Si tenemos que almacenar elems que no tendremos que modificar usaremos tuplas,
#de lo contrario, listas
#Nos permiten formatear strings y se pueden utilizar como claves en un diccionario
#(las listas no)
#Van entre paréntesis siendo estos opcionales

miTupla=("Rafa", "Rafa", 13.234, 3)

#Imprime toda la tupla
print(miTupla[:])
#Imprime el elem de la pos 2 de la tupla
print(miTupla[2])


#Convertir  una tupla en lista:
milistatupla=list(miTupla)
print(milistatupla)
#Convertir tupla en lista
mituplalista=tuple(milistatupla)
print(mituplalista)

#Comprobar si un elem está en la tupla:
print("Rafa" in mituplalista)
#Devuelve la pos del primer elem de la tupla que tenga ese nombre
print(mituplalista.index("Rafa"))
#Cuantas veces se encuentra un elem en la tupla
print(mituplalista.count("Rafa"))
#Longitud de una tupla:
print(len(mituplalista))

#Crear una tupla unitaria:
mituplaunitaria=("Rafa",)
print(len(mituplaunitaria))

#Crear tupla sin paréntesis (también válido)
mituplasinparentesis="Rafa", 2, 34.45, False
print(mituplasinparentesis)

#Desempaquetado de tuplas
mituplaempaquetada=("Rafa", "Juanito", 56, 1)
nombre1, nombre2, numero1, numero2 = mituplaempaquetada
print(nombre1)
print(nombre2)
print(numero1)
print(numero2)