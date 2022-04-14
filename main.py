import socket
import re, uuid
from time import timezone

import json
from urllib.request import urlopen


#get ip
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

print("[=====     Details     =====]")
print("Host Name is           :  " + h_name)
print("Computer IP Address is :  " + IP_addres)
print("MAC address is         :  ", end="")
print(':'.join(re.findall('..', '%012x' %uuid.getnode())))
#check private
from ipaddress import ip_address
def IP_address(IP: str)-> str:
    return "Private" if (ip_address(IP).is_private)else "Public"
if __name__ == '__main__':
    print(IP_addres + " is " + IP_address(IP_addres))
    #check ip
try:
   socket.inet_aton(IP_addres)
   print("Valid IP address")
except socket.error:
   print("Invalid IP")
  
 
#get location
#fetch the contents of a URL to handler
ip=IP_addres
res = urlopen("http://ipwhois.app/json/"+ip)
#read the contents from the handler
content = res.read()
print("\n\n> IP  address ", [ ip ] , "details : ",content)


#external ip
external_ip = urlopen('https://ident.me').read().decode('utf8')
print("\n\n> Public IP " , [ external_ip ], "details : ")
res1 = urlopen("http://ipwhois.app/json/" + external_ip + "?objects=city,region,country,isp,timezone,country_phone,latitude,longitude,type,country_flag,success,message")
content = res1.read()
print("\n",content)

