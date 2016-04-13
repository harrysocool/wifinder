import os
import sys
import nmap                         # import nmap.py
import time
import re


try:
    nm = nmap.PortScanner()         # instance of nmap.PortScanner
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

nm = nmap.PortScanner()
nm.scan(hosts='192.168.0.1/24', arguments='-n -sP -PE -T5')

for host in nm.all_hosts():
    # print('----------------------------------------------------')
    # print('Host : %s (%s)' % (host, nm[host].hostname()))
    # print('State : %s' % nm[host].state())
    print(nm[host]['vendor'])
