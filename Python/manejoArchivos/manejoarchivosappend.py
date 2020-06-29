from io import open

archivo_texto=open("archivo.txt", "a")

archivo_texto.write("\Estamos agregando una línea") #escribe al final del archivo

archivo_texto.close()