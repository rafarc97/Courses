#Listas: equivalente o casi a los arrays/arreglos/vectores en otros lenguajes

#En Pyhton las listas pueden almacenar valores de distinto tipo de datos
# a diferencia de otros lenguajes
#Se pueden expandir dinámicamente


miLista=["Amanda", "Rafa", True, 12.45, 8]
#Imprime toda la lista
print(miLista[:])
#IMprime el elem en pos 2 de la lista
print(miLista[2])
#Índice negativos empieza a contar desde el último
print(miLista[-2])
#Acceder a una porción de la lista (el 0 inclusive y el 2 exclusive)
print(miLista[0:2])
#Desde la pos 0 inclusive hasta la 2 exclusive
print(miLista[:2])
#Desde la pos 1 inclusive hasta la 2 exclusive
print(miLista[1:2])
##Imprime desde la pos 1 hasta el final ambos inclusive
print(miLista[1:])


#Añade un elem al final
miLista.append(3)
#Añadir un elem. en pos. específica
miLista.insert(2, "Roberto")
#Añadir conj. elems. al final
miLista.extend(["Juan", "Pepe"])


#Imprime la pos. del primer elem. que encuentre con dicho nombre
print(miLista.index("Juan"))
#Imprimir True o False si un elem está en la lista
print(3 in miLista)
print("Nacho" in miLista)


#Borrar elem de una lista

#Borra el elem que contenga "Juan"
miLista.remove("Juan")
#Borra el elem que contenga el nº 3
miLista.remove(3)
#Borra último elem de una lista
miLista.pop()


#Unión de listas
miLista1=["rafa", "fran"]
miLista2=[2,3]
miLista3=miLista1+miLista2
print(miLista3[:])

#Multiplicación de listas
miLista3=miLista3*3
print(miLista3[:])