from io import open

archivo_texto=open("archivo.txt", "w") #abrimos en modo escritura
frase="Estupendo día para estudiar Python \n el miércoles"
archivo_texto.write(frase) #escribimos al principio del archivo
archivo_texto.close()

