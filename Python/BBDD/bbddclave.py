import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

# la triple comilla simple se utiliza para poner instrucciones que van
#a ser muy largas
miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[
    ("AR01", "pelota", 20, "jugueteria"),
    ("AR02", "pantalón", 15, "confección"),
    ("AR03", "destornillador", 25, "ferretería"),
    ("AR04", "jarrón", 45, "cerámica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

#si intentamos insertar algun registro AR0-4 no nos dejará pq es campo clave
# /llave primaria y no pueden haber dos con el mismo nombre de registro
#aunque en la práctioca, lo qu es la construccion del campo clave y la
#insercion del campo clave esto se suele automatizar, ya que en una BBDD grande
#no podremos recordar que AR0x está ya sioendo utilizado o cual no, para que este
#Para que los campos se vayan añadiendo al AR05, AR06 sucesivamente sin tener que indicarlo
#hacemos lo siguiente:

#la linea de codigo:

#CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,

# se sustituye por:

#ID INTEGER PRIMARY KEY AUTOINCREMENT,

#despues de esto, cuando creemos la lista, el campo "AR01", y los demás
#no tendremos que introducirlos, ya que se irán incrementando solos. Por lo
#tanto luego en el miCursor.executemany(".....(?,?,?) tendremos que poner NULL
# en el primer interrogante indicando que ese campo se va a autoañadir, así:

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)



miConexion.commit()

miConexion.close()