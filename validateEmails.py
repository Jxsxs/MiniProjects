from validate_email import validate_email
import DNS
import pymysql.cursors

DNS.defaults['server']=['8.8.8.8', '8.8.4.4', '208.84.0.53', '84.200.69.80']

#=================== CONEXION A MYSQL=================
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='campos',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM table2 where COL2 is not null"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            # print(row['COL2'])
            email = row['COL2']
            # check_mx=True,verify=True,
            is_valid = validate_email(email,check_mx=True, verify=True, smtp_timeout=240)
            if is_valid:
                query_valid = "insert into table2 (COL3) values (%s)"
                cursor.execute(query_valid, (email))
                connection.commit()
                print(email + " Existe")
            else:
                print(email + " No existe")


finally:
    connection.close()
# =======================================================
