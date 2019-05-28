import pyodbc
import psycopg2
import psycopg2.extras
import pprint
import time
from datetime import datetime as dt

# ===============================================================
# Aca se hace la conexion a postgres
conn = psycopg2.connect(database='tlcmvdb' , user='postgres', password='star2018',host='172.16.126.193')
cursorPost = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# ================================================================
fechaInicial = ""
comandos = ["SOFULL", "SCTEXT", "SFARST", "SOAUTH", "SCFULL", "SCENTL", "SQCARD", "SDPROA", "SDENTL"]
# while True:
cursorPost.execute("select CAST(fechacomando as TIMESTAMP) as fechainicial from conteocomandos order by fechainicial desc limit 1")
i = 0
#leer Registros desde sql
rowPost = cursorPost.fetchall()
for colPost in rowPost:
    fechaInicial = colPost[0]
    if str(fechaInicial) == "" or not(str(fechaInicial) is None):
        cursorPost.execute("select (CAST('"+str(fechaInicial)+"' as TIMESTAMP) + CAST('60 minutes' as INTERVAL))")
        rowTime = cursorPost.fetchall()
        for colTime in rowTime:
            fechaInicial = colTime[0]

if fechaInicial == "" or fechaInicial is None:
    cursorPost.execute("select CAST(logdate as TIMESTAMP) as fechainicial from logsmscommands order by fechainicial asc limit 1")
    i = 0
    #leer Registros desde sql
    rowPost = cursorPost.fetchall()
    for colPost in rowPost:
        fechaInicial = colPost[0]

conn.commit()
while True:
    print("============== " + str(fechaInicial) + " ====================\n")
    cursorPost.execute("select CAST(logdate as TIMESTAMP) as fechainicial from logsmscommands order by fechainicial desc limit 1")
    rowFechaOrigen = cursorPost.fetchall()
    for colFechaOrigen in rowFechaOrigen:
        fechaOrigen = colFechaOrigen[0]
    if fechaInicial <= fechaOrigen:
        for comando in comandos:
            cursorPost.execute("select CAST('"+ str(fechaInicial) +"' as TIMESTAMP) as fechainicial, '"+comando+"' as comando ,count(plaincommand) as cantidad from logsmscommands where logdate between CAST('"+str(fechaInicial)+"' as TIMESTAMP) and (CAST('"+str(fechaInicial)+"' as TIMESTAMP) + CAST('60 minutes' as INTERVAL)) and plaincommand like '"+comando+"%'")
            row = cursorPost.fetchall()
            for col in row:
                print("fechaInicial: " + str(col[0]) + "|" + "Comando: " + str(col[1]) + "|" + "Conteo: " + str(col[2]))
                cursorPost.execute("insert into conteocomandos (fechacomando, comando, conteocomando) values('%s','%s',%s)" % (str(col[0]),str(col[1]),str(col[2])))

        cursorPost.execute("select (CAST('"+str(fechaInicial)+"' as TIMESTAMP) + CAST('60 minutes' as INTERVAL))")
        rowTime = cursorPost.fetchall()
        for colTime in rowTime:
            fechaInicial = colTime[0]
        conn.commit()
        # i += 1
        time.sleep(1)
    else:
        print("Nada en la db origen!")
        print("Esperando 5 minutos...")
        time.sleep(300)

#imprimir registros
# conn.commit()
# print("ultimo: " + str(fechaInicial))
# time.sleep()
