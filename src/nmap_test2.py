"""
Uso: Escaneo con nmap
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Abril 2020
"""

import nmap
 
begin = 20
end = 30

target = '192.168.100.73' #Cambialo por tu red interna

puertos = str(begin)
scanner = nmap.PortScanner() 
   
for i in range(begin,end+1):
    res = scanner.scan(target,str(i))
    print("Salida en formato CSV\n\n",scanner.csv())


