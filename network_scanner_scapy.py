# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 11:23:41 2020

@author: ASUS
"""

import scapy.all as scapy 
  
request = scapy.ARP() 
print(request.summary())
print(request.show())
  
request.pdst = '192.168.0.1/24'
broadcast = scapy.Ether() 
  
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
request_broadcast = broadcast / request 
clients = scapy.srp(request_broadcast, timeout = 1)[0] 
for element in clients: 
    print(element[1].psrc + "      " + element[1].hwsrc) 