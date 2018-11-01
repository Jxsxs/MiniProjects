import os, time
import psycopg2 
import psycopg2.extras
import csv
from os import listdir

conn = psycopg2.connect(database='bitrate' , user='postgres', password='star2018', host='172.16.126.193')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

tmp = 0
penultimo = ''
ruta = 'C:\\PerfLogs\\Admin\\EMM_Playout\\'
carpeta = ''
for cosa in listdir(ruta):
	if os.path.isdir(ruta + cosa):
		carpeta = ruta + cosa
		fechaCarpeta = os.stat(carpeta).st_mtime
		fechaTmp = os.stat(tmp).st_mtime
		# print ('carp: ' + str(carpeta) + ' '  + fechaCarpeta)
		# print ('tmp: ' + str(tmp) + ' ' + fechaTmp)
		# if tmp == cosa:
		# 	print (cosa + ' - ' + fechaCarpeta)
		# else:
		if fechaCarpeta > fechaTmp:
			penultimo = tmp
			tmp = carpeta
			fechaCarpeta = os.stat(carpeta).st_mtime
			fechaTmp = os.stat(tmp).st_mtime

# print('pen: ' + penultimo)
# print('ultimo ' + carpeta)
archivoLocalizado = ''
for archivo in listdir(penultimo):
	# print(archivo)
	archivoLocalizado = archivo
print(penultimo + '/' + archivoLocalizado)
f = open(penultimo + '/' + archivoLocalizado)

dataCsv = csv.reader(f, delimiter=',')
evitaHeader = next(dataCsv)

for row in dataCsv:
	cur.execute("insert into ancho (date, cola, high, low, medium, rate_kbps) values (%s,%s,%s,%s,%s,%s)", row)
conn.commit()
cur.close()
conn.close()
f.close()