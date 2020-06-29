#GENERADORES

def generaPares(limite):
    num=1
    miLista=[]

    while num<limite:
        miLista.append(num*2)
        num+=1
    return miLista

print(generaPares(10))

#Ahora lo hacemos con generadores:

def generaPares(limite):
    num=1

    while num<limite:
        yield num*2
        num+=1

devuelvePares=generaPares(10)

for i in devuelvePares:
    print(i)

#Para imprimir solo un elemento del while de la funcion
print(next(devuelvePares))
print("Aquí podría ir más código")
print(next(devuelvePares))
print("Aquí podría ir más código")
#Entre cada una de las llamadas a la función, esta entra en un estado de suspensión
#la cual provoca que se pare el flujo en yield.
#Esto es mucho más eficiente que hacerlo con listas puesto que de esta forma no
#necesitaríamos crear toda la lista completa (recorrer el while completo) para
#recibir los 3 primeros parámetros de dichaos elementos


#INSTRUCCIÓN yield from: se utilizan para simplificar el código de los generadores
#en el caso de utilizar bucles anidados

def devuelve_ciudades(*ciudades): #el asterisco indica que se van a recibir un nº
                                    #indefinido de argumentos, y que además se recibirán
                                   #en forma de tupla
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

#Este ej se puede hacer con yield from mucho más simplificado
#elimianmos el segundo bucle y ponemos yield from elemento

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
        yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))