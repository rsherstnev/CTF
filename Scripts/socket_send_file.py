import socket

HOST = '192.168.0.195'
PORT = 6969
FILE = 'hello.txt'

s = socket.socket()
s.connect((HOST, PORT))

with open(FILE, "rb") as f:
    while True:
        buffer = f.read(4096)
        if buffer:
            s.sendall(buffer)
        else:
            break

s.close()
