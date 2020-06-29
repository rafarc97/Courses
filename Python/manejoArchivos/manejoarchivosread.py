from io import open

archivo_texto=open("archivo.txt", "r") #abrimos en modo lectura
texto=archivo_texto.read() #leemos el archivo y almacenamos en texto
archivo_texto.close()
print(texto)

