"""
Uso: Escaneo con nmap
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Abril 2020
"""

import nmap
import os
from datetime import datetime

clear = lambda: os.system("cls" if os.name=="nt" else "clear")

def main():
    try:
        while True:
            print(datetime.now(), '\033[0;32m [INFO] Ejemplo > 192.168.100.0-24 \033[0;0m')
            ip = input('Ingresar las IPs a escanear > ')
            if ip:
                break
            clear()
            print(datetime.now(), '\033[0;31m [INFO] El rango de las IPs es un dato obligatorio \033[0;0m')
        scanner = nmap.PortScanner()
        print(datetime.now(), '\033[0;32m [INFO] Escaneando... \033[0;0m')
        scanner.scan(ip,arguments='--open')
        for host in scanner.all_hosts():
            print('--------------------------------------------------------------------------------------')
            print(datetime.now(), '\033[0;32m [INFO] Host: %s \033[0;0m' % (host))
            print(datetime.now(), '\033[0;32m [INFO] State: %s \033[0;0m' % scanner[host].state())
            for proto in scanner[host].all_protocols():
                print('--------------------------------------------------------------------------------------')
                print(datetime.now(), '\033[0;36m [INFO] Protocol: %s \033[0;0m' % proto)
                lport = scanner[host][proto].keys()
                for port in lport:                    
                    print(datetime.now(), '\033[0;36m [INFO] Port: %s\tState: %s\tName: %s\033[0;0m' % (port, scanner[host][proto][port]['state'], scanner[host][proto][port]['name']))
        
        file = open('nmap.csv','w')
        file.write(scanner.csv())
    
    except Exception as error:
        print(datetime.now(), '\033[0;91m [ERROR] Ha ocurrido un error ')
        print(error)
    except KeyboardInterrupt:
        quit()  
    
if __name__ == '__main__':
    clear()
    main()