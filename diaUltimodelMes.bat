    @Echo OFF
     
    Set "month=%date:~3,2%"
     
    :: Elimino el posible "0" y convierto la variable a numérica.
    If "%month:~0,1%" EQU "0" (Set /A "month=%month:~1%")
     
    :: Le resto un mes.
    Set /A "month-=1"
     
    :: Si el dígito es "0" (Enero-1), cambiamos a "12" (Diciembre)
    If %month% EQU 0 (Set /A "month=12")
     
    :: Si el mes solo tiene un dígito (1...9) le añadimos un "0", e
    :: indiferentemente convertimos la variable a string.
    If %month% LSS 10 (Set "month=0%month%") Else (Set "month=%month%")
     
    Echo mes %month%
     
    Pause&Exit /B 0