#CAPTURA O CONTROL DE EXCEPCIÓN

def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		

	try: #se intenta, si no ejecuta el except y luego se ejecutará el resto del programa
		return num1/num2
	except ZeroDivisionError: #para que se ejecute debe dar ese error
		print("No se puede dividir entre 0")
		return "Operación errónea"


while True:
	try:
		op1=(int(input("Introduce el primer numero: ")))
		op2=(int(input("Introduce el segundo nomero: ")))
		break;
	except ValueError:
		print("Los valores introducidos no son correctos. Try again.")


operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")


#OTRO EJEMPLO:
#se puede no especificar el tipo de except, aunque no es recomendable
def divide():
	try:
		op1=(float(input("Introduce el primero numero: ")))
		op2 =(float(input("Introduce el segundo numero: ")))
		print("La division es: " + str(op1/op2))
	except ValueError:
		print("El valor introducido es erróneo")
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
	finally: #indica que se va a ejecutar siempre pase lo que pase
		print("Calculo finalizado")

divide()

#si tenemos una funcion con solo try: y queremos que se ejecute algo que esté
#fuera dese try pero dentro de la funcion deberemos poner finally, de lo
#contrario, si el try falla, no se ejectutara el resto de codigo de la funcion


#LANZAMIENTO DE EXCEPCIONES con RAISE (sintáxiss)
#en estos ejemplos somos nosotros los que creamos excepciones propias,
# en lugar de ser el sistema quien nos lo envía, aunque esto tendrá utilidad
#sabiendo sobre POO


def evaluaEdad(edad):
	if edad<0:
		raise TypeError("No se permiten edades negativas") #raise /
	# nos permite personalizar el mensaje enviado al usuario
	if edad<20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "Cuídate..."

print(evaluaEdad(-15))
#si se ejecuta el raise el codigo que vendria a continuacion no se
# / ejecutaria
#podríamos indicar otro tipo de error el cual esté definido en la biblioteca
# de python por ejemplo si ponemos MipropioError("mensaje"), esto nos daria
# un error. Más adelante aprenderemos a crear clases personalizadas con el
#nombre que queramos y programar dentro de esa clase el código que queramos
#que se ejecute cuando se prodouzca dicha excepción


#OTRO EJEMPLO:

import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError("El numero no puede ser negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))

try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)
print("Programa terminado")