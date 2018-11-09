import pyodbc
import psycopg2
import psycopg2.extras
import pprint
import time

# se crea la conexion hacia la base de datos de sqlServer
server = 'DBSERVER'
database = 'MCASDB'
username = 'sa'
password = '@dmin123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
cursorSql = cnxn.cursor()
# ===============================================================
# Aca se hace la conexion a postgres
conn = psycopg2.connect(database='tlcmvdb' , user='postgres', password='star2018',host='172.16.126.193')
cursorPost = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# ================================================================
ultimoId = "0"
while True:
    cursorPost.execute("select logid from logsmscommands order by logid desc limit 1")

    #leer Registros desde sql
    rowPost = cursorPost.fetchall()

    for colPost in rowPost:
        ultimoId = colPost[0]

    #Consultar la Base de datos desde Sql
    cursorSql.execute("select top 1000 * FROM LogSMSCommands where logId > " + str(ultimoId) + " order by logId asc") #logSMSCommands
    rowSql = cursorSql.fetchall()
    for colSql in rowSql:
        print(colSql[0])
        cursorPost.execute("insert into logsmscommands(logid, logdate, logclientip,logclientport ,smsoperatortag, scserialnumber, cmdid, logresult, plaincommand, actualserialnumber) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", colSql)

    #imprimir registros
    conn.commit()
    print("ultimo: " + str(ultimoId))
    time.sleep(60)
