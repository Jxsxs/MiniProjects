import psycopg2 
import psycopg2.extras

conn = psycopg2.connect(database='bitrate' , user='postgres', password='star2018', host='172.16.126.193')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


cur.execute("select * from commands order by date_command asc ")
rows = cur.fetchall()

# Se declaran los valores anteriores para posteriormente restarlos
scentl_succ_anterior = 0
scfull_succ_anterior = 0
sctext_succ_anterior = 0
sdentl_succ_anterior = 0
sdproa_succ_anterior = 0
sfarst_succ_anterior = 0
soauth_succ_anterior = 0
soentl_succ_anterior = 0
sofull_succ_anterior = 0

scentl_un_anterior = 0
scfull_un_anterior = 0
sctext_un_anterior = 0
sdentl_un_anterior = 0
sdproa_un_anterior = 0
sfarst_un_anterior = 0
soauth_un_anterior = 0
soentl_un_anterior = 0
sofull_un_anterior = 0
#=========================

scentl_succ_total = 0
scfull_succ_total = 0
sctext_succ_total = 0
sdentl_succ_total = 0
sdproa_succ_total = 0
sfarst_succ_total = 0
soauth_succ_total = 0
soentl_succ_total = 0
sofull_succ_total = 0

scentl_un_total = 0
scfull_un_total = 0
sctext_un_total = 0
sdentl_un_total = 0
sdproa_un_total = 0
sfarst_un_total = 0
soauth_un_total = 0
soentl_un_total = 0
sofull_un_total = 0

x = 1
for row in rows:

	# comandos tomados de la db
	date_command = row[1]
	
	scentl_succ = row[2]
	scfull_succ = row[3]
	sctext_succ = row[4]
	sdentl_succ = row[5]
	sdproa_succ = row[6]
	sfarst_succ = row[7]
	soauth_succ = row[8]
	soentl_succ = row[9]
	sofull_succ = row[10]
	
	scentl_un = row[11]
	scfull_un = row[12]
	sctext_un = row[13]
	sdentl_un = row[14]
	sdproa_un = row[15]
	sfarst_un = row[16]
	soauth_un = row[17]
	soentl_un = row[18]
	sofull_un = row[19]
	#----------------------------
	
	if int(scentl_succ_anterior) > int(scentl_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		scentl_succ_total = scentl_succ

	if int(scfull_succ_anterior) > int(scfull_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		scfull_succ_total = scfull_succ

	if int(sctext_succ_anterior) > int(sctext_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sctext_succ_total = sctext_succ

	if int(sdentl_succ_anterior) > int(sdentl_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sdentl_succ_total = sdentl_succ
	if int(sdproa_succ_anterior) > int(sdproa_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sdproa_succ_total = sdproa_succ
	if int(sfarst_succ_anterior) > int(sfarst_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sfarst_succ_total = sfarst_succ
	if int(soauth_succ_anterior) > int(soauth_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
	
		soauth_succ_total = soauth_succ
	if int(soentl_succ_anterior) > int(soentl_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		soentl_succ_total = soentl_succ
	if int(sofull_succ_anterior) > int(sofull_succ):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sofull_succ_total = sofull_succ
	if int(scentl_un_anterior) > int(scentl_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		scentl_un_total = scentl_un
	if int(scfull_un_anterior) > int(scfull_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		scfull_un_total = scfull_un
	if int(sctext_un_anterior) > int(sctext_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sctext_un_total = sctext_un
	if int(sdentl_un_anterior) > int(sdentl_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sdentl_un_total = sdentl_un
	if int(sdproa_un_anterior) > int(sdproa_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sdproa_un_total = sdproa_un
	if int(sfarst_un_anterior) > int(sfarst_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sfarst_un_total = sfarst_un
	if int(soauth_un_anterior) > int(soauth_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		soauth_un_total = soauth_un
	if int(soentl_un_anterior) > int(soentl_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		soentl_un_total = soentl_un
	if int(sofull_un_anterior) > int(sofull_un):
		print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
		sofull_un_total = sofull_un
	else:
	
		if int(scentl_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			scentl_succ_anterior = scentl_succ

		if int(scfull_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			scfull_succ_anterior = scfull_succ

		if int(sctext_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sctext_succ_anterior = sctext_succ

		if int(sdentl_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sdentl_succ_anterior = sdentl_succ
		if int(sdproa_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sdproa_succ_anterior = sdproa_succ
		if int(sfarst_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sfarst_succ_anterior = sfarst_succ
		if int(soauth_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
			soauth_succ_anterior = soauth_succ
		if int(soentl_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			soentl_succ_anterior = soentl_succ
		if int(sofull_succ_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sofull_succ_anterior = sofull_succ
		if int(scentl_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			scentl_un_anterior = scentl_un
		if int(scfull_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			scfull_un_anterior = scfull_un
		if int(sctext_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sctext_un_anterior = sctext_un
		if int(sdentl_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sdentl_un_anterior = sdentl_un
		if int(sdproa_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sdproa_un_anterior = sdproa_un
		if int(sfarst_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			sfarst_un_anterior = sfarst_un
		if int(soauth_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			soauth_un_anterior = soauth_un
		if int(soentl_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
			
			soentl_un_anterior = soentl_un
		if int(sofull_un_anterior) == 0:
			print(x , " date_command = " , date_command , "scentl_succ = " , int(scentl_succ))
		
			sofull_un_anterior = sofull_un

		
		scentl_succ_total = float(scentl_succ) - float(scentl_succ_anterior)
		scfull_succ_total = float(scfull_succ) - float(scfull_succ_anterior)
		sctext_succ_total = float(sctext_succ) - float(sctext_succ_anterior)
		sdentl_succ_total = float(sdentl_succ) - float(sdentl_succ_anterior)
		sdproa_succ_total = float(sdproa_succ) - float(sdproa_succ_anterior)
		sfarst_succ_total = float(sfarst_succ) - float(sfarst_succ_anterior)
		soauth_succ_total = float(soauth_succ) - float(soauth_succ_anterior)
		soentl_succ_total = float(soentl_succ) - float(soentl_succ_anterior)
		sofull_succ_total = float(sofull_succ) - float(sofull_succ_anterior)
		
		scentl_un_total = float(scentl_un) - float(scentl_un_anterior)
		scfull_un_total = float(scfull_un) - float(scfull_un_anterior)
		sctext_un_total = float(sctext_un) - float(sctext_un_anterior)
		sdentl_un_total = float(sdentl_un) - float(sdentl_un_anterior)
		sdproa_un_total = float(sdproa_un) - float(sdproa_un_anterior)
		sfarst_un_total = float(sfarst_un) - float(sfarst_un_anterior)
		soauth_un_total = float(soauth_un) - float(soauth_un_anterior)
		soentl_un_total = float(soentl_un) - float(soentl_un_anterior)
		sofull_un_total = float(sofull_un) - float(sofull_un_anterior)

		# print( date_command , int(scentl_succ_total)), scfull_succ_total, sctext_succ_total,sdentl_succ_total,sdproa_succ_total,sfarst_succ_total, soauth_succ_total,soentl_succ_total,sofull_succ_total)
		# print("scentl_succ = " , row[11] , "scfull_succ = ", row[12], "sctext_succ = ",row[13],"sdentl_succ = ",row[14],"sdproa_succ = ",row[15],"sfarst_succ = ",row[16], "soauth_succ = ",row[17],"soentl_succ = ",row[18],"sofull_succ = ",row[19])
		# print("date_command: " , row[1])

		# Se asigna el valor actual a una variable nueva para tener el valor anterior 
		scentl_succ_anterior = scentl_succ
		scfull_succ_anterior = scfull_succ
		sctext_succ_anterior = sctext_succ
		sdentl_succ_anterior = sdentl_succ
		sdproa_succ_anterior = sdproa_succ
		sfarst_succ_anterior = sfarst_succ
		soauth_succ_anterior = soauth_succ
		soentl_succ_anterior = soentl_succ
		sofull_succ_anterior = sofull_succ

		scentl_un_anterior = scentl_un
		scfull_un_anterior = scfull_un
		sctext_un_anterior = sctext_un
		sdentl_un_anterior = sdentl_un
		sdproa_un_anterior = sdproa_un
		sfarst_un_anterior = sfarst_un
		soauth_un_anterior = soauth_un
		soentl_un_anterior = soentl_un
		sofull_un_anterior = sofull_un

	# Final de todos los if	
	cur.execute("insert into commands_total (date_command_total,scentl_succ_total, scfull_succ_total,sctext_succ_total,sdentl_succ_total,sdproa_succ_total,"+
		"sfarst_succ_total,soauth_succ_total,soentl_succ_total,sofull_succ_total,scentl_un_total,scfull_un_total,sctext_un_total,sdentl_un_total,sdproa_un_total,"+
		"sfarst_un_total,soauth_un_total,soentl_un_total,sofull_un_total)"+
		"values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (date_command ,int(scentl_succ_total) , int(scfull_succ_total) ,  
		int(sctext_succ_total), int(sdentl_succ_total) , int(sdproa_succ_total) ,int(sfarst_succ_total),
		int(soauth_succ_total),  int(soentl_succ_total) , int(sofull_succ_total), 
		int(scentl_un_total),  int(scfull_un_total),  int(sctext_un_total),  int(sdentl_un_total),
		int(sdproa_un_total),  int(sfarst_un_total),  int(soauth_un_total),  int(soentl_un_total),  int(sofull_un_total))) 
	conn.commit()

	x += 1

conn.close()