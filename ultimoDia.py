import calendar 
import time

mes = time.strftime("%m")
ano = time.strftime("%Y")

ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
print (ultimo_dia)
	