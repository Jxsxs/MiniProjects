import os
import psycopg2 
import psycopg2.extras
import io
import csv

conn = psycopg2.connect(database='tlcmvdb' , user='postgres', password='star2018', host='localhost')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# cur.execute("select sn from blacklist")
# print ("DataBase: " + '\n') 


# damos la ruta de la carpeta compartida en nuestro server
path = 'shared' 
lstFiles = []

lsDir = os.walk(path)
f = open('shared/report.txt')
dataCsv = csv.reader(f)
# cur.copy_from(dataCsv, 'packages', columns=('serial_number','sms_operator','sector_number','region','product_tag','product_status','product_expired','product_duration','nationality'), sep=",")
cur.execute("truncate table packages cascade")
conn.commit()
for row in dataCsv:
	cur.execute("insert into packages (serial_number, sms_operator, sector_number, region, product_tag, product_status, product_expired, product_duration, nationality) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)
# cur.execute("insert into packages (serial_number, sms_operator, sector_number, region, product_tag, product_status, product_expired, product_duration, nationality) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)", ("2141061287", "TLCM","0","ZC","BSC","0","0","10","MEX"))
conn.commit()
cur.close()
conn.close()
f.close()

#dataCsv.close()

# leemos todos los archivos de la carpeta compartida 
# y guardamos los nombres en el array

for root, dirs, files in lsDir:
	for fichero in files:
		(nombreFichero, extension) = os.path.splitext(fichero)
		if (extension == ".txt"):
			lstFiles.append(nombreFichero+extension)     
		
# se recorre el array para buscar cada uno de los archivos
# print ("Archivo" + '\n')
# for row in cur:
# 	serial_db = str(row['sn'])
# 	print("db: " + serial_db)
for x in (lstFiles):
	os.remove('shared/'+x)
		# dato_archivo = open('shared/'+x,"r",encoding="utf-8")
		# lineas = dato_archivo.readlines()
		# for linea in lineas:
		# 	linea = linea.split(",",1)
		# 	serial_file = linea[0]
		# 	if serial_db == serial_file:
		# 		print("Aqui hay uno : " + serial_file + " file:" + x)
		# 	# print("file: " + serial_file)
		# 	# linea.next()
		# dato_archivo.close()
		
