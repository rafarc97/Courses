from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)
miFrame.pack()

#declaramos la variable operacion para que pueda ser utilizada en las funciones
operacion=""
reset_pantalla=False
resultado=0 #aqui se almacenaran los resultados de las operaciones realizadas
#-----------------INTERFAZ---------------------------------------
#-----------------PANTALLA---------------------------------------
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla) #para que dicho widget esté
#relacionado con la variable numeroPantalla
pantalla.grid(row=1,column=1,padx=10,pady=10, columnspan=4) #el columnspan se hace para que
#la pantalla ocupe 4 columnas
pantalla.config(background="black", fg="#03f943", justify="right")

def numeroPulsado(num):
    #con esto le decimos que le añada a la pantalla lo que le pasemos
    # + lo que tenía
    global operacion
    global reset_pantalla

    if reset_pantalla != False:
        numeroPantalla.set(num)
        reset_pantalla=False
    else:
        numeroPantalla.set(numeroPantalla.get()+num)
    #si pulsamos el boton suma, se coloca en pantalla solo el boton del numero pulsado

#almacenaremos en num lo que hay en pantalla antes de pulsar la tecla num, ya que luego
#se soobreescribirá con el segundo numero a sumar
def suma(num):
    #declaramos una variable global a pesar de estar declarado dentro de esta funcion
    global operacion
    global resultado
    resultado+=int(num) #usamos la funcion int puesto que todo lo que se introduce en el cuadro
    #de texto negro que estamos usando para mostrar los numeros que pulsamos son strings
    operacion="suma"
    reset_pantalla=True
    numeroPantalla.set(resultado)

num1=0
contador_resta=0

def resta(num):
    global operacion
    global resultado
    global num1
    global contador_resta
    global reset_pantalla

    if contador_resta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_resta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_resta = contador_resta + 1
    operacion = "resta"
    reset_pantalla = True


contador_multi=0

def multiplicar(num):
    global operacion
    global resultado
    global num1
    global contador_multi
    global reset_pantalla

    if contador_multi == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contador_multi == 1:
            resultado = num1 * int(num)
        else:
            resultado = int(resultado) * int(num)
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_multi = contador_multi + 1
    operacion = "multiplicacion"
    reset_pantalla = True


contador_divi=0

def dividir(num):
    global operacion
    global resultado
    global num1
    global contador_divi
    global reset_pantalla

    if contador_divi == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contador_divi == 1:
            resultado = num1 / float(num)
        else:
            resultado = float(resultado) / float(num)

        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contador_divi = contador_divi + 1
    operacion = "division"
    reset_pantalla = True


def el_resultado():
    global resultado
    global operacion
    global contador_resta
    global contador_multi
    global contador_divi

    if operacion == "suma":
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
        resultado = 0
    elif operacion == "resta":
        numeroPantalla.set(int(resultado) - int(numeroPantalla.get()))
        resultado = 0
        contador_resta = 0
    elif operacion == "multiplicacion":
        numeroPantalla.set(int(resultado) * int(numeroPantalla.get()))
        resultado = 0
        contador_multi = 0
    elif operacion == "division":
        numeroPantalla.set(int(resultado) / int(numeroPantalla.get()))
        resultado = 0
        contador_divi = 0

#------------------FILA 1----------------------------------------
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:dividir(numeroPantalla.get()))
botonDiv.grid(row=2,column=4)

#------------------FILA 2----------------------------------------
# haciendo command=numeroPulsado("4") estaríamos haciendo una llamada
# automátrica a la función al ejecutar el programa, para que eso no ocurra
# usamos las funciones lambda
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame, text="x", width=3, command=lambda:multiplicar(numeroPantalla.get()))
botonMult.grid(row=3,column=4)

#------------------FILA 3----------------------------------------
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRest.grid(row=4,column=4)


#------------------FILA 4----------------------------------------
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=5,column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5,column=4)

raiz.mainloop()