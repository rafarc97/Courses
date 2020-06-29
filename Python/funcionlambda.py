#consiste en resumir una funcion normal que podamos
# escribir en python en una expresion lambda
#una funcion lambda no podra tener bucles ni condiciones
#lo unico que podra hacer devolvernos calculos, está diseñado
#para funciones sencillas. También son llamadas como  funciones:
#"on the go", "on demand", o "online". Son otras formas de definirlas

#def area_triangulo(base,altura):
 #   return (base*altura)/2


#imaginemos que tengamos un programa que necesita acceder muchas veces
#durante la ejecucion del programa a dicha funcion, para ello es mas comodo
#resumir la llamada a esta funcion en una funcion lambda


#creamos nuestra funcion lambda

area_triangulo=lambda base,altura:(base*altura)/2
print(area_triangulo(5,7))

#otro ejemplo:

destacar_valor=lambda comision: "!{} EUROS!".format(comision)

comision_Pablo=15587

print(destacar_valor(comision_Pablo))