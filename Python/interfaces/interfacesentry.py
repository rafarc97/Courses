from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()


#grid se utiliza para formularios
#para alinear los textos utilizamos sticky N, ne, e,se, s, sw, w, nw (agujas del reloj)
#para añadir un padding en pixeles entre los elementos podemos agregar padx, pady

#creamos esta variable que será la utilizada en la función codigoBoton
minombre=StringVar() #con esto le decimos que se trata de una cadena de caracteres

cuadroNombre=Entry(miFrame, textvariable=minombre) #con textv..=minombre le decimos que va a estar asociado
#de alguna manera con la variable minombre
cuadroNombre.grid(row=0,column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center") #el texto que escribamos aparece en rojo y centrado

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1, padx=10, pady=10)
cuadroPass.config(show="*", justify="center")#aparece * cuando escribirmos, podemos usar cualquier otro caracter

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1, padx=10, pady=10)
cuadroApellido.config(justify="center")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1, padx=10, pady=10)
cuadroDireccion.config(justify="center")

textoComentarios=Text(miFrame,width=16,height=5)
textoComentarios.grid(row=4,column=1, padx=10, pady=10)

 #si queremos escribir mas de lo quie cabe en el texto, dicho widget añade
#scrolling autopmatico, es decir se hace mas cuadro la caja de texto autom. pero
scrollVert=Scrollbar(miFrame, command=textoComentarios.yview) #construimos un objeto
#de tipo scrollbar vertical

#la añadimos a la interfaz
scrollVert.grid(row=4, column=2, sticky="nsew", ) #con el sticky hacemos que la barra nos permita
#mover tambien el texto, no solo con las flechas del scrollbar.

# Luego para que la barra se adapte
#al lugar donde se está escribiendo en cada momento debemos añadir el comando :
textoComentarios.config(yscrollcommand=scrollVert.set)

#####

nombreLabel=Label(miFrame,text="Comentarios:")
nombreLabel.grid(row=1,column=0,sticky="e", padx=10, pady=10)

passLabel=Label(miFrame,text="Contraseña:")
passLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame,text="Direccion:")
direccionLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame,text="Comentarios:")
comentariosLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)

def codigoBoton():
    minombre.set("Rafa")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton) #codigoBoton sera la funcion que haga cosas
#cuando pulsemos el boton. En concreto escribirá Rafa en el cuadro Nombre
botonEnvio.pack()


raiz.mainloop()