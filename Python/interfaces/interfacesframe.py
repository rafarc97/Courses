#handy reference (documentación oficial de python)
from tkinter import *

raiz=Tk()
raiz.title("Ventana de Pruebas")
#raiz.resizable(True,False)
#raiz.iconbitmap("icono.ico")
raiz.geometry("650x350")
raiz.config(bg="green")
miFrame=Frame()
miFrame.pack()

miFrame.config(bg="orange") #para que se vea debemos darle tamaño, no a la raiz, sino al frame
#la raiz se adaptarña al tamaño del frame
miFrame.config(width="650",height="350") #ahora al redimensionar la raiz vemos ambos colores

#como cambiar posicionamientos por defecto del frame
#miFrame.pack(side="right") #frame se queda anclado a la derecha de la raiz
#también podremos usar top, bottom o left
#miFrame.pack(side="right", anchor="n") #para manejar que se posicione tb al norte, sur este u oeste
#miFrame.pack(fill="x")#el frame se expande horizontalmente
#miFrame.pack(fill="y", expand="True") #para que se expanda verticalmente (necesitamos expand)
#miFrame.pack(fill="both",expand="True") #para que se expanda hori. y vert.

miFrame.config(bd=35)
miFrame.config(relief="groove") #tipo de borde especial, para que se note debemos darle antes un ancho al borde
#miFrame.config(relief="sunker") #otro tipo de borde

#miFrame.config(cursor="hand2") #cambiamos tipo de cursor cuando el cursor se posiciona sobre el frame
miFrame.config(cursor="pirate") #otro tipo de cursor


#a la raiz tambien podemos darle un bd, relief y cursor
raiz.config(bd=55)
raiz.config(relief="sunken")
raiz.config(cursor="hand2")


raiz.mainloop()