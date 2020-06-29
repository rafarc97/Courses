#También denominada GUI
#Tendremos una raíz(tk), dentro de ella el Frame y dentro de él, los widgets (botones)
#también a veces se le llama widgets al conjunto taiz(tk) + frame
#le ponemos una w .py para que no habra la terminal cuando se ejecute el archivo con su interfaz

from tkinter import *

raiz=Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(0,0) #le decimos false al width y false al height, ahora no se podrá
#redimensionar la ventana. podemos poner un 1 en cualquier de los 2 campos para permitir
#redimensionar a lo ancho/alto. También se puede usar True/False.
raiz.iconbitmap("elnaxo.xbm")

raiz.geometry("650x350") #ancho x alto
raiz.config(bg="blue") #fondo azul



raiz.mainloop() #para que la ventana este presente debe estar en un bucle infinito (estará
# a la escucha de los eventos), por eso siempre estará al final

