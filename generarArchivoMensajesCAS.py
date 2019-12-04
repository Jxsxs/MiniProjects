import pandas as pd
import pyodbc
import psycopg2
import psycopg2.extras
from pandas import ExcelWriter
import time
import xlsxwriter

import csv

with open('example.csv', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)



#conexion a base de datos postgres
# ====================================
# conn = psycopg2.connect(database='pairing' , user='postgres', password='star2018',host='172.16.126.193')
# cursorPost = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# # =====================================
# idPagando = []
# cdsnPagando = []
# snPagando = []
# activosPagando = []
# inactivosPagando = []
# actualPagando = []
# statusPagando = []
# paquetesPagando = []
# cascdsnPagando = []
# # Se agrega cada dataFrame para cada sheet
# # activos pagando
# print("1.- activos pagando")
# cursorPost.execute("select * from resultado where resultado.actual='ON' and resultado.activos=resultado.paquetes;")
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     idPagando.append(colPost[0])
#     cdsnPagando.append(colPost[1])
#     snPagando.append(colPost[2])
#     activosPagando.append(colPost[3])
#     if colPost[4] is None:
#         inactivosPagando.append("")
#     else:
#         inactivosPagando.append(colPost[4])
#     actualPagando.append(colPost[5])
#     statusPagando.append(colPost[6])
#     paquetesPagando.append(colPost[7])
#     cascdsnPagando.append(colPost[8])
#
# # Se guardan los datos en un archivo de excel
# dfPagando = pd.DataFrame(
# {
#     'id': idPagando,
#     'cdsn': cdsnPagando,
#     'sn': snPagando,
#     'activos': activosPagando,
#     'inactivos': inactivosPagando,
#     'actual': actualPagando,
#     'status': statusPagando,
#     'paquetes':paquetesPagando,
#     'cascdsn': cascdsnPagando
# },
# columns = [
#     'id',
#     'cdsn',
#     'sn',
#     'activos',
#     'inactivos',
#     'actual',
#     'status',
#     'paquetes',
#     'cascdsn'
# ])
#
#
# # Cambio de paquete en proceso
# print("2.- Cambio de paquete en proceso")
# cursorPost.execute("select * from resultado where resultado.actual='ON' and resultado.activos!=resultado.paquetes and paquetes not like '%DEM%' and paquetes is not null;")
# idCambio = []
# cdsnCambio = []
# snCambio = []
# activosCambio = []
# inactivosCambio = []
# actualCambio = []
# statusCambio = []
# paquetesCambio = []
# cascdsnCambio = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     idCambio.append(colPost[0])
#     cdsnCambio.append(colPost[1])
#     snCambio.append(colPost[2])
#     activosCambio.append(colPost[3])
#     inactivosCambio.append(colPost[4])
#     actualCambio.append(colPost[5])
#     statusCambio.append(colPost[6])
#     paquetesCambio.append(colPost[7])
#     cascdsnCambio.append(colPost[8])
#
# # Se guardan los datos en un archivo de excel
# dfCambio = pd.DataFrame(
# {
#     'id': idCambio,
#     'cdsn': cdsnCambio,
#     'sn': snCambio,
#     'activos': activosCambio,
#     'inactivos': inactivosCambio,
#     'actual': actualCambio,
#     'status': statusCambio,
#     'paquetes':paquetesCambio,
#     'cascdsn': cascdsnCambio
# },
# columns = [
#     'id',
#     'cdsn',
#     'sn',
#     'activos',
#     'inactivos',
#     'actual',
#     'status',
#     'paquetes',
#     'cascdsn'
# ])
#
# # Activos con demo
# print("3.- Activos con demo")
# cursorPost.execute("select * from resultado where resultado.actual='ON' and resultado.activos!=resultado.paquetes and paquetes like '%DEM%' and paquetes is not null;")
# idActivosDemo = []
# cdsnActivosDemo = []
# snActivosDemo = []
# activosActivosDemo = []
# inactivosActivosDemo = []
# actualActivosDemo = []
# statusActivosDemo = []
# paquetesActivosDemo = []
# cascdsnActivosDemo = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     idActivosDemo.append(colPost[0])
#     cdsnActivosDemo.append(colPost[1])
#     snActivosDemo.append(colPost[2])
#     activosActivosDemo.append(colPost[3])
#     inactivosActivosDemo.append(colPost[4])
#     actualActivosDemo.append(colPost[5])
#     statusActivosDemo.append(colPost[6])
#     paquetesActivosDemo.append(colPost[7])
#     cascdsnActivosDemo.append(colPost[8])
#
# # Se guardan los datos en un archivo de excel
# dfActivosDemo = pd.DataFrame(
# {
#     'id': idActivosDemo,
#     'cdsn': cdsnActivosDemo,
#     'sn': snActivosDemo,
#     'activos': activosActivosDemo,
#     'inactivos': inactivosActivosDemo,
#     'actual': actualActivosDemo,
#     'status': statusActivosDemo,
#     'paquetes':paquetesActivosDemo,
#     'cascdsn': cascdsnActivosDemo
# },
# columns = [
#     'id',
#     'cdsn',
#     'sn',
#     'activos',
#     'inactivos',
#     'actual',
#     'status',
#     'paquetes',
#     'cascdsn'
# ])
#
# # Activos en proceso
# print("4.- Activos en proceso")
# cursorPost.execute("select *  from resultado where resultado.actual='ON'  and resultado.paquetes is NULL;")
# idActivosProceso = []
# cdsnActivosProceso = []
# snActivosProceso = []
# activosActivosProceso = []
# inactivosActivosProceso = []
# actualActivosProceso = []
# statusActivosProceso = []
# paquetesActivosProceso = []
# cascdsnActivosProceso = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     idActivosProceso.append(colPost[0])
#     cdsnActivosProceso.append(colPost[1])
#     snActivosProceso.append(colPost[2])
#     activosActivosProceso.append(colPost[3])
#     inactivosActivosProceso.append(colPost[4])
#     actualActivosProceso.append(colPost[5])
#     statusActivosProceso.append(colPost[6])
#     paquetesActivosProceso.append(colPost[7])
#     cascdsnActivosProceso.append(colPost[8])
#
# # Se guardan los datos en un archivo de excel
# dfActivosProceso = pd.DataFrame(
# {
#     'id': idActivosProceso,
#     'cdsn': cdsnActivosProceso,
#     'sn': snActivosProceso,
#     'activos': activosActivosProceso,
#     'inactivos': inactivosActivosProceso,
#     'actual': actualActivosProceso,
#     'status': statusActivosProceso,
#     'paquetes':paquetesActivosProceso,
#     'cascdsn': cascdsnActivosProceso
# },
# columns = [
#     'id',
#     'cdsn',
#     'sn',
#     'activos',
#     'inactivos',
#     'actual',
#     'status',
#     'paquetes',
#     'cascdsn'
# ])
#
# # Inactivos
# print("5.- Inactivos")
# cursorPost.execute("Select * from resultado where resultado.actual='OFF' and resultado.paquetes is NULL;")
# idInactivos = []
# cdsnInactivos = []
# snInactivos = []
# activosInactivos = []
# inactivosInactivos = []
# actualInactivos = []
# statusInactivos = []
# paquetesInactivos = []
# cascdsnInactivos = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     idInactivos.append(colPost[0])
#     cdsnInactivos.append(colPost[1])
#     snInactivos.append(colPost[2])
#     activosInactivos.append(colPost[3])
#     inactivosInactivos.append(colPost[4])
#     actualInactivos.append(colPost[5])
#     statusInactivos.append(colPost[6])
#     paquetesInactivos.append(colPost[7])
#     cascdsnInactivos.append(colPost[8])
#
# # Se guardan los datos en un archivo de excel
# dfInactivos = pd.DataFrame(
# {
#     'id': idInactivos,
#     'cdsn': cdsnInactivos,
#     'sn': snInactivos,
#     'activos': activosInactivos,
#     'inactivos': inactivosInactivos,
#     'actual': actualInactivos,
#     'status': statusInactivos,
#     'paquetes':paquetesInactivos,
#     'cascdsn': cascdsnInactivos
# },
# columns = [
#     'id',
#     'cdsn',
#     'sn',
#     'activos',
#     'inactivos',
#     'actual',
#     'status',
#     'paquetes',
#     'cascdsn'
# ])
#
# # Desconexion en proceso
# print("6.- Desconexion en proceso")
# cursorPost.execute("select count(id) from resultado where resultado.actual='OFF' and resultado.paquetes is not NULL;")
# contDesconexion = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     contDesconexion.append(colPost[0])
#
# # Se guardan los datos en un archivo de excel
# dfDesconexion = pd.DataFrame(
# {
#     'Conteo': contDesconexion
# },
# columns = [
#     'Conteo'
# ])
#
#
# # clasificacion de inactivos pos status en SAC
# print("7.- clasificacion de inactivos pos status en SAC")
# cursorPost.execute("select estatus,count(estatus) as cantidad from resultado where resultado.actual='OFF' and resultado.paquetes is NULL group by estatus;")
# statusInactivosStatus = []
# cantidadInactivosStatus = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     statusInactivosStatus.append(colPost[0])
#     cantidadInactivosStatus.append(colPost[1])
#
# # Se guardan los datos en un archivo de excel
# dfInactivosStatus = pd.DataFrame(
# {
#     'status': statusInactivosStatus,
#     'cantidad': cantidadInactivosStatus
# },
# columns = [
#     'status',
#     'cantidad'
# ])
#
#
# # clasificacion de desconexion en proceso por status en SAC
# print("8.- clasificacion de desconexion en proceso por status en SAC")
# cursorPost.execute("select estatus,count(estatus) as cantidad from resultado where resultado.actual='OFF' and resultado.paquetes is not NULL group by estatus;")
# statusDesconexionStatus = []
# cantidadDesconexionStatus = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     statusDesconexionStatus.append(colPost[0])
#     cantidadDesconexionStatus.append(colPost[1])
#
# # Se guardan los datos en un archivo de excel
# dfDesconexionStatus = pd.DataFrame(
# {
#     'status': statusDesconexionStatus,
#     'cantidad': cantidadDesconexionStatus
# },
# columns = [
#     'status',
#     'cantidad'
# ])
#
#
# # =================ALMACENES==================
# # Distribuidores
# print("9.- Distribuidores")
# cursorPost.execute("select * from almacen_distribuidores")
# cdsnDistribuidores = []
# statusDistribuidores = []
# almacenDistribuidores = []
# distribuidorDistribuidores = []
# paqueteDistribuidores = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     cdsnDistribuidores.append(colPost[0])
#     statusDistribuidores.append(colPost[1])
#     almacenDistribuidores.append(colPost[2])
#     distribuidorDistribuidores.append(colPost[3])
#     paqueteDistribuidores.append(colPost[4])
#
# # Se guardan los datos en un archivo de excel
# dfDistribuidores = pd.DataFrame(
# {
#     'cdsn': cdsnDistribuidores,
#     'status': statusDistribuidores,
#     'almacen': almacenDistribuidores,
#     'distribuidor':distribuidorDistribuidores,
#     'paquete':paqueteDistribuidores
# },
# columns = [
#     'cdsn',
#     'status',
#     'almacen',
#     'distribuidor',
#     'paquete'
# ])
#
# # Limbo
# print("10.- Limbo")
# cursorPost.execute("select * from almacen_limbo;")
# cdsnLimbo = []
# paqueteLimbo = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     cdsnLimbo.append(colPost[0])
#     paqueteLimbo.append(colPost[1])
#
# # Se guardan los datos en un archivo de excel
# dfLimbo = pd.DataFrame(
# {
#     'cdsn': cdsnLimbo,
#     'paquete': paqueteLimbo
# },
# columns = [
#     'cdsn',
#     'paquete'
# ])
#
# # Principal
# print("11.- Principal")
# cursorPost.execute("select * from almacen_principal;")
# cdsnPrincipal = []
# statusPrincipal = []
# almacenPrincipal = []
# paquetePrincipal = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     cdsnPrincipal.append(colPost[0])
#     statusPrincipal.append(colPost[1])
#     almacenPrincipal.append(colPost[2])
#     paquetePrincipal.append(colPost[3])
#
# # Se guardan los datos en un archivo de excel
# dfPrincipal = pd.DataFrame(
# {
#     'cdsn': cdsnPrincipal,
#     'status': statusPrincipal,
#     'almacen': almacenPrincipal,
#     'paquete':paquetePrincipal
# },
# columns = [
#     'cdsn',
#     'status',
#     'almacen',
#     'paquete'
# ])
#
# # Tecnicos
# print("12.- Tecnicos")
# cursorPost.execute("select * from almacen_tecnicos;")
# cdsnTecnicos = []
# statusTecnicos = []
# almacenTecnicos = []
# distribuidorTecnicos = []
# paqueteTecnicos = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     cdsnTecnicos.append(colPost[0])
#     statusTecnicos.append(colPost[1])
#     almacenTecnicos.append(colPost[2])
#     distribuidorTecnicos.append(colPost[3])
#     paqueteTecnicos.append(colPost[4])
#
# # Se guardan los datos en un archivo de excel
# dfTecnicos = pd.DataFrame(
# {
#     'cdsn': cdsnTecnicos,
#     'status': statusTecnicos,
#     'almacen': almacenTecnicos,
#     'distribuidor':distribuidorTecnicos,
#     'paquete':paqueteTecnicos
# },
# columns = [
#     'cdsn',
#     'status',
#     'almacen',
#     'distribuidor',
#     'paquete'
# ])
# # ========================================
# # Cuenta de activos por almacen
# print("13.- Cuenta de activos por almacen")
# cursorPost.execute("select count(*)  as cuenta , 'activos'  from almacen_distribuidores where paquete is not null union select count(*) as cuenta , 'inactivos'  from almacen_distribuidores where paquete is null;")
# cuenta1 = []
# cuenta2 = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     cuenta1.append(colPost[0])
#     cuenta2.append(colPost[1])
#
# # Se guardan los datos en un archivo de excel
# dfActivosAlmacen = pd.DataFrame(
# {
#     'cuenta1': cuenta1,
#     'cuenta2': cuenta2
# },
# columns = [
#     'cuenta1',
#     'cuenta2'
# ])
#
#
# # cuenta de status y activo
# print("14.- cuenta de status y activo")
# cursorPost.execute("select count(cdsn) as cantidad, estatus, 'si' as activo from almacen_distribuidores where paquete is not null group by estatus union select count(cdsn) as cantidad, estatus, 'no' as activo from almacen_distribuidores where paquete is null group by estatus order by estatus desc;")
# cantidadStatusActivo = []
# statusStatusActivo = []
# activoStatusActivo = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     cantidadStatusActivo.append(colPost[0])
#     statusStatusActivo.append(colPost[1])
#     activoStatusActivo.append(colPost[2])
#
#
# # Se guardan los datos en un archivo de excel
# dfStatusActivo = pd.DataFrame(
# {
#     'cantidad': cantidadStatusActivo,
#     'status': statusStatusActivo,
#     'activo': activoStatusActivo
#
# },
# columns = [
#     'cantidad',
#     'status',
#     'activo'
# ])
#
# # inexistentes CAS
# print("15.- inexistentes CAS")
# cursorPost.execute("select almacentodas.* from almacentodas left join stbs on stbs.cdsn=almacentodas.cdsn where stbs.cdsn is null;")
# cdsnInexistentes = []
# validaInexistentes = []
# #leer Registros desde postgres
# rowPost = cursorPost.fetchall()
# for colPost in rowPost:
#     cdsnInexistentes.append(colPost[0])
#     validaInexistentes.append(colPost[1])
#
# # Se guardan los datos en un archivo de excel
# dfInexistentes = pd.DataFrame(
# {
#     'cdsn': cdsnInexistentes,
#     'valida': validaInexistentes
# },
# columns = [
#     'cdsn',
#     'valida'
# ])
# # -------------------------------------------------------------
# fecha = time.strftime("%Y-%m-%d")
# # En el writer se especifica el nombre del documento
# writer = ExcelWriter('conciliacion-%s.xlsx' % fecha, engine='xlsxwriter')
# # Despues se incluye el nombre de cada sheet y se pasa el writer creado anteriormente
# dfPagando.to_excel(writer, sheet_name='activos_pagando', index=False)
# dfCambio.to_excel(writer, sheet_name='cambio_paquete_proceso', encoding='utf-8', index=False)
# dfActivosDemo.to_excel(writer, sheet_name='activos_con_demo', encoding='utf-8',index=False)
# dfActivosProceso.to_excel(writer, sheet_name='activacion_en_proceso', encoding='utf-8',index=False)
# dfInactivos.to_excel(writer, sheet_name='inactivos', encoding='utf-8',index=False)
# dfDesconexion.to_excel(writer, sheet_name='descon_en_proceso', encoding='utf-8',index=False)
# dfInactivosStatus.to_excel(writer, sheet_name='clasi_inactivos_SAC', encoding='utf-8',index=False)
# dfDesconexionStatus.to_excel(writer, sheet_name='clasi_desconexion_SAC', encoding='utf-8',index=False)
# dfDistribuidores.to_excel(writer, sheet_name='almacen_distribuidores', encoding='utf-8',index=False)
# dfLimbo.to_excel(writer, sheet_name='almacen_limbo', encoding='utf-8',index=False)
# dfPrincipal.to_excel(writer, sheet_name='almacen_principal',encoding='utf-8', index=False)
# dfTecnicos.to_excel(writer, sheet_name='almacen_tecnicos', encoding='utf-8',index=False)
# dfActivosAlmacen.to_excel(writer, sheet_name='cuenta_activos_almacen', encoding='utf-8',index=False)
# dfStatusActivo.to_excel(writer, sheet_name='cuenta_status_activo', encoding='utf-8',index=False)
# dfInexistentes.to_excel(writer, sheet_name='inexistentes_CAS', encoding='utf-8',index=False)
# print("generado")
# # Al final solo se invoca al metodo save que es para guardar el archivo
# writer.save()
# print("====================================================================")
# print("Archivo Completo!")
