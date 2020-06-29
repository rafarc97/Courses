from tkinter import *
from tkinter import messagebox #para poder usar las ventanas emergentes
import sqlite3


root =Tk()

miFrame=Frame(root,width=1200,height=800)
miFrame.pack()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=600)


# --------------------- FUNCIONES BOTONES/PESTAÑAS --------------------------

def conectarBBDD():
    try:
        miConexion = sqlite3.connect("Primera BBDD")
        miCursor = miConexion.cursor()
        miCursor.execute('''CREATE TABLE DATOS_USUARIOS (ID INTEGER PRIMARY KEY, 
                NOMBRE_USUARIO VARCHAR(30), PASSWORD VARCHAR(30), APELLIDO VARCHAR(30),
                DIRECCION VARCHAR(30), COMENTARIOS VARCHAR(100))''')

        messagebox.showinfo("BBDD", "BBDD creada con éxito")

    except:
        messagebox.showwarning("!Atención!", "La BBDD ya existe")


def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    if valor=="yes":
        root.destroy()


def borrarCampos():
    #con esto borramos de la pantalla todos los campos, pq estamos colocando cadenas vacias
    miNombre.set("")
    miID.set("")
    miApellido.set("")
    miDireccion.set("")
    miPass.set("")
    #con esto le indico que debe borrar desde el primer caracter hasta el final
    textoComentarios.delete(1.0,END)


def crearRegistro():
    miConexion = sqlite3.connect("Primera BBDD")
    miCursor = miConexion.cursor()

    #Parametrización de consultas: esto evita la inyección sql

    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentarios.get("1.0",END)
    miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL,?,?,?,?,?)",(datos))

    """
    miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, '" + miNombre.get() +
                     "','" + miPass.get() +
                     "','" + miApellido.get() +
                     "','" + miDireccion.get() +
                     "','" + textoComentarios.get("1.0", END) + "')")
    """
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leerRegistro():
    miConexion = sqlite3.connect("Primera BBDD")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" + miID.get())
    elUsuario = miCursor.fetchall()

    for usuario in elUsuario:
        miID.set(usuario[0])
        miNombre.set(usuario[1])
        miPass.set(usuario[2])
        miApellido.set(usuario[3])
        miDireccion.set(usuario[4])
        textoComentarios.insert(1.0, usuario[5])

    miConexion.commit()


def actualizarRegistro():
    miConexion = sqlite3.connect("Primera BBDD")
    miCursor = miConexion.cursor()

    #Aplicamos parametrización:

    datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textoComentarios.get("1.0",END)

    miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?  " +
    "WHERE ID=" + miID.get(),(datos))
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito")

"""
    miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_USUARIO= '"+ miNombre.get() +
    "', PASSWORD='" + miPass.get() +
     "', APELLIDO='" + miApellido.get() +
     "', DIRECCION='" + miDireccion.get() +
     "', COMENTARIOS='" + textoComentarios.get("1.0", END) +
     "' WHERE ID=" + miID.get())
"""


def borrarRegistro():
    miConexion = sqlite3.connect("Primera BBDD")
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID=" + miID.get())
    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito")


def infoAdicional():
    messagebox.showinfo("Procesador de Rafa", "Procesador de textos version 2.0")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia GNU Linux")


#--------------------- PESTAÑA BBDD --------------------------
archivoBBDD=Menu(barraMenu, tearoff=0)
archivoBBDD.add_command(label="Conectar", command=conectarBBDD)
archivoBBDD.add_command(label="Salir",command=salirAplicacion)


#--------------------- PESTAÑA BORRAR -------------------------
borrarMenu=Menu(barraMenu,tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrarCampos)


#--------------------- PESTAÑA CRUD ----------------------------
archivoCRUD=Menu(barraMenu,tearoff=0)
archivoCRUD.add_command(label="Crear", command=crearRegistro)
archivoCRUD.add_command(label="Leer", command=leerRegistro)
archivoCRUD.add_command(label="Actualizar", command=actualizarRegistro)
archivoCRUD.add_command(label="Borrar", command=borrarRegistro)


#---------------------- PESTAÑA AYUDA --------------------------
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)



#añadimos las pestañas
barraMenu.add_cascade(label="BBDD", menu=archivoBBDD)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=archivoCRUD)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

# ------------------------- FORMULARIO ------------------------
miID=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=1,column=1, padx=10, pady=10)
cuadroID.config(fg="red", justify="center")

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=2,column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=3,column=1, padx=10, pady=10)
cuadroPass.config(show="*", justify="center")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=4,column=1, padx=10, pady=10)
cuadroApellido.config(justify="center")

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=5,column=1, padx=10, pady=10)
cuadroDireccion.config(justify="center")


textoComentarios=Text(miFrame,width=16,height=5)
textoComentarios.grid(row=6,column=1, padx=10, pady=10)

scrollVert=Scrollbar(miFrame, command=textoComentarios.yview)


scrollVert.grid(row=4, column=2, sticky="nsew", )

textoComentarios.config(yscrollcommand=scrollVert.set)



idLabel=Label(miFrame,text="Id:")
idLabel.grid(row=1,column=0,sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=2,column=0,sticky="e", padx=10, pady=10)

passLabel=Label(miFrame,text="Contraseña:")
passLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=5,column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=6,column=0, sticky="e", padx=10, pady=10)


# ------------------------- BOTONES --------------------------
miFrame2=Frame(root)
miFrame2.pack()

BotonCrear=Button(miFrame2,text="Create", command=crearRegistro).pack()
#BotonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

BotonLeer=Button(miFrame2,text="Read", command=leerRegistro).pack()
#BotonLeer.grid(row=2, column=0, sticky="e", padx=10, pady=10)

BotonActualizar=Button(miFrame2,text="Update", command=actualizarRegistro).pack()
#BotonActualizar.grid(row=3, column=0, sticky="e", padx=10, pady=10)

BotonBorrar=Button(miFrame2,text="Delete", command=borrarRegistro).pack()
#BotonBorrar.grid(row=4, column=0, sticky="e", padx=10, pady=10)




root.mainloop()