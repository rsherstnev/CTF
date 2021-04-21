import socket

HOST = '192.168.0.195'
PORT = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

connection, address = s.accept()
while True:
    data = connection.recv(4096)
    if not data:
        break
    print(data)

connection.close()
s.close()
