# needed pysmb, netaddr

import sys
from nmb.NetBIOS import NetBIOS
from netaddr import IPNetwork

netbios = NetBIOS()
for ip in IPNetwork(sys.argv[1]):
    netbios_names = netbios.queryIPForName(str(ip), timeout=0.1)
    if netbios_names:
        print(', '.join(netbios.queryName(netbios_names[0], ip=str(ip)) + netbios_names))
