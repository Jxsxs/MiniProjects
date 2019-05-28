import subprocess
import sys
import pysftp
import os
import io
import time

#el host y usuario al cual se hara la conexion
HOST="-p 6630.star root@172.16.126.240"
#nos cambiamos de directorio a donde se encuntran los archivos y despues los listamos
COMMAND="cd /var/www/html/files2017/pruebaSCP ; ls"
#decimos que el directorio local sera de donde se esta ejecutando el script
path = "."
lstFiles = []

#recorre mos el directorio local y guardamos todos los archivos con extencion txt en un arreglo
lsDir = os.walk(path)
for root, dirs, files in lsDir:
    for archivo in files:
        lstFiles.append(archivo)
srv = pysftp.Connection(host="172.16.126.240", username="root",password="6630.star")
if srv:
    print("Conexion establecida\n")
else:
    sys.exit(0)
srv.cwd('/var/www/html/files2017/pruebaSCP/')
result = []
i = 0;

# Get the directory and file listing
data = srv.listdir()
# Closes the connection
# Prints out the directories and files, line by line
print("========================================")
for i in data:
    result.append(i)
    print(i)

ruta = sys.argv[1]
path = ""
path = ruta.split("\\")
sizefileLocal = os.stat(ruta).st_size
# print(str(sizefileLocal) + "\n")
#archivos en el directorio remoto
for archivo in result:
    # busqueda = str(busqueda.split("/"))
    if archivo == str(path[len(path)-1]):
        #Si el archivo que pretendemos enviar ya existe se detiene la aplicacion
        print("========================================")
        sizefileRemoto = srv.stat(archivo).st_size
        # print(sizefileRemoto)
        if sizefileLocal > sizefileRemoto:
            print("========================================")
            print("\nReemplazando %s ...." % ruta)
            srv.put(ruta,"./%s" % str(path[len(path)-1]))
            time.sleep(3)
            sys.exit(0)
        else:
            print("\nYa existe el archivo %s" % archivo)
            sys.exit(0)

print("========================================")
print("\ncopiando %s ...." % ruta)
srv.put(ruta,"./%s" % str(path[len(path)-1]))
