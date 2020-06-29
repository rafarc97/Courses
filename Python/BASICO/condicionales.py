print("Programa de evaluacion sobre notas de alumnos")

nota_alumno=input("Introduce la nota del alumno: ")

def evaluacion(nota):
    valoracion="aprobado" #estavariable es de ámbito local en la funcion
    if nota<5:
        valoracion="suspenso" #esta es local solo en el if
    return valoracion

print(evaluacion(int(nota_alumno)))

print("Programa sobre verificación de acceso")

edad_usuario = int(input("Introduce una edad, por favor: "))

if edad_usuario < 18:
    print("No puedes pasar")
elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

presidente=int(input("Introduce salario presidente: "))
print("Salario presidente: " + str(presidente))

director=int(input("Introduce salario director: "))
print("Salario director: " + str(director))

jefe=int(input("Introduce salario jefe: "))
print("Salario jefe: " + str(jefe))

administrativo=int(input("Introduce salario administrativo: "))
print("Salario administrativo: " + str(administrativo))

if presidente<director<jefe<administrativo:
    print("Todo funciona")
else:
    print("ALgo falla")

#Operador and y or

print("Programa Becas 2020: ")

distancia_escuela=int(input("Introduce la distancia a la escuela en km:"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el nº hermanos en el centro"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto"))
print(salario_familiar)

#si se cumple distancia_escuela40 y alguna de las otras dos condiciones
if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")



print("Adignaturas año 2020: ")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
asignatura=input("Escribe la asignatura escogida: ")

#python es case sensitive (sensible a mayúsculas)
if asignatura in ("Informática gráfica", "Pruebas de software", "Usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura elegida no está contemplada")


