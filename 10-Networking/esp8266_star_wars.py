# Taken from the REPL based example.
import socket


addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
server_addr = addr_info[0][-1]
s = socket.socket()
s.connect(server_addr)
while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')
