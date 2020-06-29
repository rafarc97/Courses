from tkinter import *

root=Tk()

#para almacenar cuando ppulsemos los raodiobutton y saber que imprimir
varOpcion=IntVar()


def imprimir():
    #si cuando pulsemos el radiobutton, el valor de varOpcion es 1 => se imprime
    #el mensaje en el label "etiqueta"
    if varOpcion.get()==1:
        etiqueta.config(text="has elegido masculino")
    elif varOpcion.get()==2:
        etiqueta.config(text="has elegido femenino")
    else:
        etiqueta.config(text="Has elegido otros")


#se coloca un label para indicarle al usuario sobre lo que va a elegir a continuación
Label(root,text="Género:").pack()

#root para indicarle donde se va a situar
#text para el texto que aparecerá como opción
#le asignamos una variable con un valor. Al dar valores distintos podremos
#seleccionar una de las opciones y si otro radiobotton esta seleccionado,
#se deseleccionará
#la función imprimir será llamada cuando se pulse en el botón para imprimir el mensaje
Radiobutton(root,text="Masculino", variable=varOpcion,value=1,command=imprimir).pack()
Radiobutton(root,text="Femenino",variable=varOpcion,value=2,command=imprimir).pack()
Radiobutton(root,text="Otras opciones",variable=varOpcion,value=3,command=imprimir).pack()


etiqueta=Label(root)
etiqueta.pack()


root.mainloop()