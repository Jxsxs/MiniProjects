import psycopg2 
import psycopg2.extras

conn = psycopg2.connect(database='bitrate' , user='postgres', password='star2018', host='172.16.126.193')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

if conn:
	print('Conectado')