import sqlite3

#creamos la conexion llmada miCOnexion
miConexion=sqlite3.connect("Primera BBDD")

#creamos el puntero que nos permitirá trabajar con la BBDD
miCursor=miConexion.cursor()

#trabajamos con la BBDD
#la creacion de la tabla la podremos tener solo en la primera ejecucion de este archivo
#ya quye en la segunda nos dara error al intentar crear una tabal con el mismo nombre
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER)")


miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15)")

#Cuando vamos a insertar varias cosas, es usual utilizar listas o tuplas
#ya que es más comodo y rapido

#variosProductos=[
 #   ("Camiseta", 10),
  #  ("Jarron", 90),
   # ("Camión", 10000)
#]

#cone sto insertamos la lista
#insertamos tantos "?" como campos tenga los elementos de la lista
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?)", variosProductos)



#para obtener un lote de registros tambien necesitamos crear una lista para
#almacenarlos y poder verlos
miCursor.execute("SELECT * FROM PRODUCTOS")

#el metodo fetchall nos devuelve una lsita de tuplas con todos los registros
variosProductos=miCursor.fetchall()

print(variosProductos)

#tambien podemos imprimir cada tupla de la lista utilizando unbucle for:

for producto in variosProductos:
    print(producto)

    #tambien podemos imprimir el 1er elemento y 2º por separado p.ej de cada tupla
for producto in variosProductos:
    print("Nombre artículo:",producto[0], "Precio:", producto[1])

#con esta instruc. confirmamos lo cambios realizados en el programa
miConexion.commit()

#cerramos la conexion
miConexion.close()