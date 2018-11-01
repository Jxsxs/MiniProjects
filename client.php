<?PHP
//ESPECIFICA EL SERVIDOR AL CUAL SE VA A ACCEDER – 127.0.0.1(LOCAL)
$HOST="localhost";
 
/*SOCKET_CREATE=>CREA Y DEVUELVE UN RECURSO SOCKET*/
$SOCKET=SOCKET_CREATE(AF_INET,SOCK_STREAM,SOL_TCP);
 
//PUERTO DE COMUNICACION QUE USARA EL SOCKET
$PUERTO=80;
 
/*SOCKET_CONNECT=>INICIA UNA CONEXIÓN HACIA ADDRESS $HOST EL RECURSO $SOCKET*/
$CONEXION=SOCKET_CONNECT($SOCKET,$HOST,$PUERTO);
 
$TAMAÑO=2000;
IF($CONEXION){
    ECHO "CONEXION EXITOSA, PUERTO ".$PUERTO."\N\N";
    $BUFFER="BYTES, (".$HOST.") \R\N"; //MENSAJE A ENVIAR AL SERVIDOR
    $SALIDA="";
    //BUFFER->TRABAJA CON ALMACENAMIENTO DE MEMORIA
    SOCKET_WRITE($SOCKET,$BUFFER);
 
    WHILE($SALIDA=SOCKET_READ($SOCKET,$TAMAÑO)){
        ECHO "</BR>".$SALIDA;
    }
 
    }ELSE{
    ECHO "\N LA CONEXION TCP NO SE A PODIDO REALIZAR, PUERTO: ".$PUERTO;
    }
 
SOCKET_CLOSE($SOCKET); //CIERRA EL RECURSO SOCKET DADO POR $SOCKET


?>

<!-- $port = 80;

$output="datatatatatatta" ;

$socket1 = socket_create(AF_INET, SOCK_STREAM,0) or die("Could not create socket\n");

socket_connect ($socket1 , $host,$port ) ;

socket_write($socket1, $output, strlen ($output)) or die("Could not write output\n");

socket_close($socket1) ;


?> --> 

<!-- <?php include('shelper.php');

$sockethelper = new sockethelper('localhost',80);
$sockethelper->send_data('Hello World');
echo $sockethelper->read_data();
$sockethelper->close_socket();
?> -->