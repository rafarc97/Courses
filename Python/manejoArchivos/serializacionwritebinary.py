import pickle

lista_nombres=["Rafa", "Pedro", "Juan", "Fran" ]
fichero_binario=open("lista_nombres", "wb") #write binary
pickle.dump(lista_nombres,fichero_binario) #volcado lista al fichero extero
fichero_binario.close() #cerramos el fichero binario
del(fichero_binario) #lo borramos de la memoria RAM

#para guardar datos en una DDBB se suele codificar en binario
#antes de transferirlo a dicha DDBB