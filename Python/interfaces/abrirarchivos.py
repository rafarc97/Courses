from tkinter import *
#hay funcioens que a no ser que la importemos a parte como filedialog u otras
#no podremos utilizar
from tkinter import filedialog

root=Tk()


def abreFichero():
    #usamos el objeto filedialog para llamar al metodo askopenfilename para almecenar
    #en fichero la ruta del archivo que queremos abrir
    #podemos especificarle desde donde queremos que se abra con initialdir
    #podemos indicarle los tipos de archivos que queramos que se represente para posteriormente
    #proceder a escogerlo y abrirlo. Esto nos permite que solo se visualicen los directorios
    #y los arhcivos que sean formato .c o .txt. Es una manera de filtrar. AUnque podemos filtrar
    #tantos tipos de ficheros como queramos añadiendo nuevas tuplas.
    fichero=filedialog.askopenfilename(title="Abrir",initialdir="/",filetypes=
    (("Fichero de C", "*.c"),("Ficheros de texto","*.txt")))

    print(fichero) #esto nos imprime la ruta del archivo que seleccionemos


#boton que nos llevará a abrir el filedialog cuando pulsemos
Button(root,text="Abrir fichero", command=abreFichero).pack()



root.mainloop()