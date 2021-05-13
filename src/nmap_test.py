"""
Uso: Escaneo con nmap
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 08 Abril 2020
"""

import nmap

# take the range of ports to  
# be scanned 
begin = 79
end = 80
  
# assign the target ip to be scanned to 
# a variable 
target = '192.168.100.1'#148.234.5.0/24
   
# instantiate a PortScanner object 
scanner = nmap.PortScanner() 
   
for i in range(begin,end+1): 
   
    # scan the target port 
    res = scanner.scan(target,str(i))
    print(type(res))
    for x,y in res.items():
        print(x,y)
   
    # the result is a dictionary containing  
    # several information we only need to 
    # check if the port is opened or closed 
    # so we will access only that information  
    # in the dictionary 
    res = res['scan'][target]['tcp'][i]['state']
   
    print(f'port {i} is {res}.')
