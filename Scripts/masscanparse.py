#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print('Usage: masscanparse.py <FILE>')
else:
    tcp = list()
    udp = list()
    with open(sys.argv[1]) as file:
        for line in file.readlines():
            data = line.split()
            if data[0] == 'open':
                if data[1] == 'tcp':
                    tcp.append(int(data[2]))
                else:
                    udp.append(int(data[2]))
    tcp.sort()
    udp.sort()
    print('-p T:', end='')
    for port in tcp:
        print('{},'.format(port), end='')
    udp_string = str()
    print('U:', end='')
    for port in udp:
        udp_string = udp_string + '{},'.format(port)
    print(udp_string.rstrip(','))
