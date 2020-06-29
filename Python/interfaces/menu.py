from tkinter import *

root =Tk()

#con esto creamos el menu y lo situamos en la parte superior de nuestro root
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


#ahora tendremos que determinar que elementos tendrá nuestro menú

#creamos el elemento internamente para el programa
#para quitar unas lineas horizontales que ssalen por defecto al pulsar una de las pestañas
#(la cual se llama tearoff lagrimas en ingles), se pone a 0 y se elimina
archivoMenu=Menu(barraMenu, tearoff=0)
#ahora creamos los elementos que estarán dentro de cada pestaña con add_command:
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
#agregamos una barra horizontal que separe el de arriba de el abajo
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu,tearoff=0)


archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia")
archivoAyuda.add_command(label="Acerca de...")




#en label introducimos lo que queremos que salga en la int. grafica en representacion
#de ese elemento de la barra de menu.
#con add_cascade logramos añadirlo
#con menu=archivoMenu le indicamos el elemento al que hacemos referencia

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()