from io import open
archivo_texto=open("archivo.txt", "r+")   #r+ lectura/escritura
archivo_texto.seek(11) #se situa en el caracter 11
print(archivo_texto.read())  #lee desde el 1 hasta final, y deja puntero al final
archivo_texto.seek(0) #se situa en el caracter 0
print(archivo_texto.read(14))#imprime del caracter 0 al 14 y deja puntero en 14
archivo_texto.seek(len(archivo_texto.read())/2)#situa el puntero en medio de los carac
print(archivo_texto.read())
archivo_texto.seek(len(archivo_texto.readline()))#situa puntero al final de la primera linea
#readline lee el texto por lineas
print(archivo_texto.read())
archivo_texto.seek(0)
#DISTINGUIR readline de readlines
lista_texto=archivo_texto.readlines()
lista_texto[1]="Linea incluida desde el exterior";
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()