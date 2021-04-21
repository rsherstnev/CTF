#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print('Usage: masscanparse.py <FILE>')
else:
    tcp = list()
    udp = list()
    with open(sys.argv[1]) as report:
        for line in report.readlines():
            data = line.split()
            if data[0] == 'open':
                tcp.append(int(data[2])) if data[1] == 'tcp' else udp.append(int(data[2]))                
    result = ''
    if tcp:
        result += '-sS '
        tcp.sort()
    if udp:
        result += '-sU '
        udp.sort()
    if tcp or udp:
        result += '-p '
    if tcp:
        result += 'T:'
        for port in tcp:
            result += '{},'.format(port)
    if udp:
        result += 'U:'
        for port in udp:
            result += '{},'.format(port)
    print(result.rstrip(','))
