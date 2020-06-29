<!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Document</title>

    <style>
    
        table {
            width: 50%;
            border: 1px dotted red;
            margin: auto;
        }
    
    </style>
 </head>
 <body>

 <?php

    require("datosConexion.php");
    $conexion=mysqli_connect($db_host,$db_usuario,$db_contra);

    if(mysqli_connect_errno()){
        echo"Fallo al conectar con la BBDD";
        exit();
    }

    mysqli_select_db($conexion, $db_nombre) or die ("No se encuentra la BBDD");
   
    mysqli_set_charset($conexion,"utf8");

    $consulta="SELECT * FROM ARTÍCULOS WHERE PAÍSDEORIGEN='ESPAÑA'";

    $resultados = mysqli_query($conexion,$consulta);

    $fila=mysqli_fetch_row($resultados);


    while($fila=mysqli_fetch_row($resultados)){

        echo "<table width = '50%' align='center' border = '1'><tr><td>";

        echo $fila[0] . " </td><td> ";
        echo $fila[1] . " </td><td> ";
        echo $fila[2] . " </td><td> ";
        echo $fila[3] . " </td><td> ";
        echo $fila[4] . " </td><td> ";
        echo $fila[5] . " </td><td> ";
        echo $fila[6] . " </td><td> </tr></table>";
        echo "<br>";
        echo "<br>";
    }

    mysqli_close($conexion);


    /* Tenemos dos formas de importar tablas en nuestra BBDD:
        Una es importando un archivo excel (ya exportado ese mismo
        a .ods con google drive por ejemplo), en el que tendremos que
        tener en cuenta si la primera fila de nuestro excel son ya datos
        de la propia tabla o si corresponde a los titulos de las
        columnas, para saber si marcar la casilla en phpymyadmin o no
        antes de importarlo.
        La otra forma es creando en un bloc de notas las instrucciones
        sql de create table... y luego las de insert into table...
        Este archivo del bloc de ntoas deberá guardarse como un .sql 
        para que al importarle en phpmyadmin lo traduzca como tal.   */

        /* Esto nos sirve para migrar datos (TABLAS) de una BBDD a otra */
?>
     
 </body>
 </html>