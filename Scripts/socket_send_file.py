import socket

HOST = '192.168.0.195'
PORT = 6969
FILE = 'hello.txt'

s = socket.socket()
s.connect((HOST, PORT))

with open(FILE, "rb") as f:
    buffer = f.read(4096)
    while buffer:
        s.sendall(buffer)
        buffer = f.read(4096)

s.close()