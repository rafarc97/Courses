nombreUsuario=input("Introduce tu nombre de Usuario: ")

print("El nombre es: ", nombreUsuario.upper())
print("El nombre es: ", nombreUsuario.lower())
print("El nombre es: ", nombreUsuario.capitalize())

#RECORDAR: todo lo introducido por teclado por input se considera texto
edad=input("Introduce una edad: ")
print(edad.isdigit()) #imprime true si tiene numero y false si tiene caracteres

while(edad.isdigit()==False):
    print("Por favor introduce un valor numerico")
    edad=input("Introduce una edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")