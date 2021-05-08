# For Scan network IP Address

import subprocess
import ipaddress
import time



starttime = time.time()
# take imput from user
ip_address = input("Enter IP Address in CIDR Format Ex.127.0.0.1/24 :")

ip_ne = ipaddress.ip_network(ip_address)

#for all host
all_host = list(ip_ne.hosts())

#for sub process
info = subprocess.STARTUPINFO()
info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = subprocess.SW_HIDE

#while True:
for i in range(len(all_host)):
    op = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_host[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]

    if "Destination Host Unreachable" in op.decode('utf-8'):
        print(str(all_host[i]), " Is Offline")
    elif "Request Time Out" in op.decode('utf-8'):
        print(str(all_host[i]), " iS Offline")
    else:
        print(str(all_host[i]), "Is online")





