from io import open

archivo_texto=open("archivo.txt", "r") #abrimos en modo lectura
lineas_texto=archivo_texto.readlines() #igual pero en forma de lista
archivo_texto.close()
print(lineas_texto)
print(lineas_texto[0])
print(lineas_texto[1])