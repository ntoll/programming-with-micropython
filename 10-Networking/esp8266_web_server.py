import machine
import socket
import json

template = """HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: {length}
Server: MicroPython

{json}"""

pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    status = {str(p): p.value() for p in pins}
    data = json.dumps(status)
    response = template.format(length=len(data), json=data)
    cl.send(response)
    cl.close()
