import socket
import re
import uuid
from urllib.request import urlopen
import json

#get ip
h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

print("[=====     Details     =====]")
print(f"Host Name              : {h_name}")
print(f"Computer IP Address    : {IP_addres}")
print(f"MAC Address            : {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")

#check private
from ipaddress import ip_address
def IP_address(IP: str) -> str:
    return "Private" if ip_address(IP).is_private else "Public"
if __name__ == '__main__':
    print(f"IP Address is          : {IP_addres} ({IP_address(IP_addres)})")

#check ip
try:
    socket.inet_aton(IP_addres)
    print("Valid IP address")
except socket.error:
    print("Invalid IP")

# external ip
external_ip = urlopen('https://ident.me').read().decode('utf8')
res1 = urlopen("http://ipwhois.app/json/" + external_ip + "?objects=city,region,country,isp,timezone,country_phone,latitude,longitude,type,country_flag,success,message")
content = res1.read()

# decode JSON response
data = json.loads(content)

# print available keys and values
print("\n\n> Public IP address details:")
print(f"    Public IP Address: {external_ip}")
print(f"    City             : {data['city']}")
print(f"    Region           : {data['region']}")
print(f"    Country          : {data['country']}")
print(f"    ISP              : {data['isp']}")
print(f"    Timezone         : {data['timezone']}")
print(f"    Country Phone    : {data['country_phone']}")
print(f"    Latitude         : {data['latitude']}")
print(f"    Longitude        : {data['longitude']}")
print(f"    Type             : {data['type']}")
print(f"    Country Flag     : {data['country_flag']}")
