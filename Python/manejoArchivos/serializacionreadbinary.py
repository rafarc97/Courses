import pickle
fichero=open("lista_nombres", "rb") #read binary
lista=pickle.load(fichero)
print(lista[:])
fichero.close()
del(fichero)
