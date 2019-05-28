import os
import io
import time

tmp = 0
cont = 0
while True:
	time.sleep(2)
	path = 'shared' 
	lstFiles = []
	lsDir = os.walk(path)
	for root, dirs, files in lsDir:
		for fichero in files:
			(nombreFichero, extension) = os.path.splitext(fichero)
			if (extension == ".txt"):
				if (nombreFichero+extension) not in lstFiles:
					lstFiles.append(nombreFichero+extension)


	if len(lstFiles) > 0:
		for x in lstFiles:
			sizeFile = os.path.getsize('shared/' + x)
			if tmp < sizeFile:
				print(sizeFile)
				tmp = sizeFile
			else:
				cont += 1
				if cont == 10:
					print("ejecuta buscaFiles.py")
					os.system("buscaFiles.py")
					tmp=0
					cont=0
					time.sleep(180)
	else:
		os.system('cls')        
