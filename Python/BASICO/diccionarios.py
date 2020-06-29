#Diccionarios: estructura de datos que nos permite almacenar
#valores de diferente tipo (enteros, cadenas de texto, decimales)
#e incluso listas y otros diccionarios
#La principal carac. es que los datos se almacenan asociados
#a una clave de tal forma que se crea una asociación de tipo
#clave:valor para cada elem. almacenado.
#Los elems almacenados no están ordenador. El orden es indiferente
#a la hora de almacenar info en un diccionario.
#Van entre llaves


midiccionario={23: "Rafa", "Amanda": 21, "Francia": "París", "España": "Madrid"}

#Imprimir todo el diccionario:
print(midiccionario)
#Imprimir el valor de la clave "Francia":
print(midiccionario["Francia"])

#Añadir elem al final del dicc.
midiccionario["Italia"]="Lisboa"

#Modificar elem del dicc. (se sobreescribe el valor)
midiccionario["Italia"]="Roma"
print(midiccionario)

#Eliminar un elem
del midiccionario["Francia"]
print(midiccionario)

#Asignación tupla a diccionario
mitupladiccionario=["Reino Unido", "Portugal"]
midiccionariotupla={mitupladiccionario[0]: "Londres", mitupladiccionario[1]: "Lisboa"}
print(midiccionariotupla)

#Otra manera de imprimir el valor de la clave de un elem
print(midiccionariotupla[mitupladiccionario[0]])

#Podemos almacenar + de 1 valor para una clave en concreto:
midiccionariovalores={"anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionariovalores["anillos"])

#Podemos almacenar un diccionario de una tupla en nuestro dicc
midiccionariodetuplas={"Rafa": 23, "anillos":{"temporadas": [1991, 1992, 1993], "fichajes": ["amanda", "pepe"]}}
print(midiccionariodetuplas)

#Imprimir claves del diccionario:
print(midiccionariodetuplas.keys())

#Imprimir valores del dicc
print(midiccionariodetuplas.values())

#Imprimir longitud del dicc (nº elems clave-valor)
print(len(midiccionariodetuplas))