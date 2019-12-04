import pandas as pd

df1 = pd.read_excel('compara_archivos_csv/export.xlsx',usecols='A',header=None, skiprows=1)
df2 = pd.read_excel('compara_archivos_csv/2019_taquillas.xlsx',usecols='A',header=None, skiprows=1)
#print(df2)

archivo1 = list()
archivo2 = list()
listaFinal = list()

for indice_fila, valorInicial in df1.iterrows():
    cadena1 = valorInicial[0].split("0",1)
    cadena2 = valorInicial[0].split("0",2)
    archivo1.append(cadena1[0]+cadena2[2])
    #print(cadena1[0]+cadena2[2])
    #valorFinal = valorFinal.replace("0","")
    #if linea not in fileone:
    #    print(linea)
for indice_fila, valorInicial in df2.iterrows():
    archivo2.append(valorInicial[0])

for datoInicial in archivo1:
    for datoFinal in archivo2:
        if datoInicial != datoFinal:
            listaFinal.append(datoInicial)


print(str(len(listaFinal)))