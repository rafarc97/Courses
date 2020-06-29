#BUCLE FOR:

for i in [1,2,3]:
    print("Hola")

for i in ["primavera","verano","otoño","invierno"]:
    print("Hola")

for i in ["primavera","verano","otoño","invierno"]:
    print(i)

for estaciones_año in ["primavera","verano","otoño","invierno"]:
    print(estaciones_año)

#con end le decimos que espacios o carac queremos que se
# impriman entre cada vuelta del bucle
for i in ["PIldoras", "Informáticas", 3]:
    print("Hola", end="")

#imprimir el valor de i de cada iteracion con espacios de separacion
for i in "rafaelrodriguezcalvente@gmail.com":
    print(i, end= " ")


contador=0
for i in "rafa@gmail.com":
    if(i == "@" or i=="."):
        ++contador
if contador==2:
    print("email correcto")
else:
    print("email incorrecto")


#utilizacion de la función range()

#imprime del 0 al 4
for i in range(5):
    print(i)


#notación para unir textos con variables f, que acepta range
for i in range(5,10): #5 inclusive 10 exclusive
    print(f"valor de la variable {i}")

for i in range(5, 50, 3): #del 5 al 49 de 3 en 3
    print(f"valor de la variable {i}")

texto="hola"
print(len(texto))

valido=False
email2=input("Introduce tu email: ")
for i in range (len(email2)):
    if email2[i]=="@":
        valido=True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")


#BUCLE WHILE:


i=1
while i<= 10:
    #para imprimir dos cadenas concatenadas usamo función str()
    print("Ejecucion " + str(i))
    i=i+1
print("Termino la ejecucion")



edad=int(input("Introduce tu edad por favor: "))
while edad <5 or edad>100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo")
    edad=int(input("INtroduce tu edad por favor: "))
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante " + str(edad))


import math

print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número por favor: "))

intentos = 0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;
    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos = intentos + 1
if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))


#BUCLES usando CONTINUE

for letra in "Python":
    if letra == "h":
        continue
print("Viendo la letra: " +  letra)




nombre= "Rafael Rodríguez"
contador=0

for i in nombre:
    if i==" ":
        continue
    contador += 1

print(contador)


#BUCLE usando PASS: lo que hace es devolver un NULL (no es muy utilizado)

#hasta que el usuario no haga ctrl+c no sale del bucle
while True:
    pass

#Representa una clase nula para indicar que existe pero se implementará later
class MiClase:
    pass


#BUCLE usando ELSE
#se utiliza con for o con while
#si el bucle da todas sus vueltas, se ejecuta dicho else, si no no.
#frecuentemente es confundido por asociarse a un if, pero ese else no tiene
#nada que ver con ningún if, sino con el bucle for/while

email=input("Introduce tu email, por favor: ")

for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False
print(arroba)
