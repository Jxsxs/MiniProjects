import pyodbc
import psycopg2
import psycopg2.extras
import pprint
import time


# se crea la conexion hacia la base de datos de sqlServer
# server = '172.16.126.20,1433\DBSERVER'
# database = 'MCASDB'
# username = 'sa'
# password = '@dmin123'
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
# cursorSql = cnxn.cursor()
# ===============================================================
# Aca se hace la conexion a postgres
conn = psycopg2.connect(database='tlcmvdb' , user='postgres', password='star2018',host='172.16.126.193')
cursorPost = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# ================================================================
ultimoId = "0"
while True:

    cursorPost.execute("select serial_number from packages where serial_number::bigint>"+ ultimoId  +"::bigint order by serial_number asc limit 5")
    #Consultar la Base de datos desde Sql
    # cursorSql.execute("select TOP (5) * FROM LogSMSCommands;") #logSMSCommands
    # ultimoDato
    #leer Registros desde sql
    row = cursorPost.fetchall()
    # row = cursorSql.fetchall()
    for col in row:
        print(col)
        ultimoId = col[0]
        # cursorPost.execute("insert into logsmscommands(log_id, log_date, log_client_ip, sms_operator_tag, sc_serial_number, cmd_id, log_result, plain_command, actual_serial_number) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", col)
    # conn.commit()
    # cursorSql.close()
    # cursorPost.close()
    # conn.close()
    # cnxn.close()
    #imprimir registros
    # pprint.pprint(row)
    # print("ultimo: " + ultimoId)
    time.sleep(10)
