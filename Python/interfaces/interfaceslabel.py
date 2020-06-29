from tkinter import *

root=Tk()
miFrame=Frame(root,width=500,height=400)
miFrame.pack()
miImagen=PhotoImage(file="1.gif")
Label(miFrame,image=miImagen).place(x=100,y=200)
#miLabel=Label(miFrame,text="Hola alumnos de Python")
#miLabel.pack()#adapta la raiz y el frame a lo que ocupe el mensaje
#para que se respeten las dimensiones del frame hacemos:
#miLabel.place(x=100,y=200)

#Esto se puede hacer de manera abreviada así:
#Label(miFrame,text="Hola alumnos de Python").place(x=100, y=200
#además para especificar el color de texto y estilo + tamaño de letra
#Label(miFrame,text="Hola alumnos de Python", fg="red", font=("Arial", 18)).place(x=100, y=200)

#la libreria trabaja porm defecto con imagenes png y gif:


root.mainloop()