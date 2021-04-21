import socket

HOST = '192.168.0.1'
PORTS = [i for i in range(1, 65536)]

for port in PORTS:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((HOST, port))
        print("\033[32m {}".format('TCP:' + str(port) + ' open'))
        s.close()
    except socket.error:
        pass
