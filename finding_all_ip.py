# import nmap

import socket

print("host-name:", socket.gethostname())
print(socket.getaddrinfo(socket.gethostname(), None))
ip_addresses = [i[4][0] for i in socket.getaddrinfo(socket.gethostname(), None)]

print(ip_addresses)
