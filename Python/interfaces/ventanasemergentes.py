from tkinter import *
from tkinter import messagebox #para poder usar las ventanas emergentes

root =Tk()

def infoAdicional():
    # método de meesagebox para mostrar informacion
    #primer campo del metodo para el titulo de la ventana y el segundo para el texto
    #que aparecera en el contenido
    messagebox.showinfo("Procesador de Rafa", "Procesador de textos version 2.0")

def avisoLicencia():
    #igual a showinfo pero cambia el icono, este no es de info es de warning
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU Linux")

def salirAplicacion():
    #nos permite responder a "yes" o "no" y enfunion de lo qe pulsemos haremos una cosa u otra
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    #esto devuelve true o false, entonces tendriamos qe poner en el if "true" o "false"
    #valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()

def cerrarDocumento():
    #funciona con True o False
    valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento Bloqueado")
    if valor==False:
        root.destroy()


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)


archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu,tearoff=0)


archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
#le añadimos la opcion de que cuando pulsemos en dicha pestaña se ejecute
#la unfioncy por lo tanto aparezca la ventana emergente
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)




barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)



root.mainloop()