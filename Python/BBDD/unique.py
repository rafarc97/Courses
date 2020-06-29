import sqlite3

miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

#al indicar unique decimos que no se repetiran datos en el campo nombre_articulo
#el unique puede estar en cualquier campo
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE, 
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')


#si pusieramos otra tupla qe repetiera pelota por ejemplo
#nos daria error de la clausula UNIQUE
productos=[
    ("pelota", 20, "jugueteria"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)


miConexion.commit()

miConexion.close()