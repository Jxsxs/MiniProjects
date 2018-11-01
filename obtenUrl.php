<?php
	// $host= $_SERVER["HTTP_HOST"];
	// $url= $_SERVER["REQUEST_URI"];
	obtenCadena();

	function obtenCadena(){
		$salida = array();
		Try{
			$nombre=$_REQUEST['name'];
			if ($nombre=="rep_2018") {
				exec('python manda.py '. $nombre , $salida);
				echo $nombre;
			}else{
				echo "access denied";
			}
		}
		catch (Exception $e) {
		    header("HTTP/1.0 404 Not Found");
		header("Status: 404 No se encontro el registro ");
		    echo 'Excepción capturada: ',  $e->getMessage(), "\n";
		}
		        
	}
	
?>