from tkinter import *
#los checkbuttons son las tipicas casillas de verificacion,
# estas nos permiten selccionar + de una a la vez

root=Tk()

root.title("Ejemplo")
root.geometry("400x400")
playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+=" playa"
    if(montagna.get()==1):
        opcionEscogida+=" montaña"
    if(turismoRural.get()==1):
        opcionEscogida+=" turismoRural"

    textoFinal.config(text=opcionEscogida)

#meter la imagne en un label nos permmitrá meter la imagen en la zona que deseamos dentro
#de nuetro frame o root
foto=PhotoImage(file="avion.png")
Label(root, image=foto, height=300, width=300).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame,text="Playa", variable=playa, onvalue=1, offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Montaña", variable=montagna, onvalue=1, offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame,text="Turismo Rural", variable=turismoRural, onvalue=1, offvalue=0,command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()


root.mainloop()