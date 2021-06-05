# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 11:35:36 2020

@author: ASUS
"""

import subprocess
devices=subprocess.check_output(['netsh','wlan','show','network'])
devices=devices.decode('ascii')
devices=devices.replace("\r","")
ssid=devices.split("\n")
ssid=ssid[4:]
ssids=[]
x=0
y=0
while x<len(ssid):
    if x%5 ==0:
        ssids.append(ssid[x])
    x+=1
while y< len(ssids):
    print(ssids)
    y+=1
        
