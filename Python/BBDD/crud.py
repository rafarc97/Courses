import sqlite3
#CRUD indica CREATE READ UPDATE DELETE, ya hemos visto el create y read
#ahora vemos update y delete

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")


#saca una lista de lo que hemos indicado anteiromente y lo introduce en productos
productos=miCursor.fetchall()
print(productos)

#si depsues de ejecutar la sioguiente ionstruccion refrescamos en Browse data de la app DB Browser
#veremos como aparece un 35 en lugar de un 20 que había antes
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")


#al borrar tenemos que tener cuidado porque si borramos por precio o seccion (que no tienen
#claves unicas podremos borrar mas de un campo, para ello borramos pos id o nombre articuloç
#que son unicos para cada campo


#CON LA CLAUSULA DELETE SIEMPRE UTILIZAR LA CLAUSULA WHERE, PQ NO HABRÁ
#MARCHA ATRÁS SI BORRAMOS TODA LA TABLA
miCursor.execute("DELETE FROM PRODUCTOS WHERE  ID=2")

miConexion.commit()

miConexion.close()