#!/usr/bin/env python
# Author : Besim ALTINOK

import sys, os
from scapy.all import *
from termcolor import colored
conf.verb = 0

toplam, beacon, probereq, proberes = 0, 0, 0, 0
ssidlist   = []
bssidlist  = []

def Parser(pkt):
	global beacon, probereq, proberes, hidden, toplam
	toplam += 1
	if pkt.haslayer(Dot11Beacon):
		ssid = pkt.info
		mac  = pkt.addr2
		beacon += 1
		if mac not in bssidlist:
			bssidlist.append(mac)
			ssidlist.append(ssid)
		
	elif pkt.haslayer(Dot11ProbeReq):
		ssid = pkt.info
		mac  = pkt.addr2
		probereq += 1
		if mac not in bssidlist:
			bssidlist.append(mac)
			ssidlist.append(ssid)

	elif pkt.haslayer(Dot11ProbeResp):
		ssid = pkt.info
		mac  = pkt.addr2
		proberes += 1
		if mac not in bssidlist:
			bssidlist.append(mac)
			ssidlist.append(ssid)	
	

if __name__ == "__main__":
	os.system("reset")
	sniff(offline="/home/rootx/Dosyalar/scapy_e.pcap", prn=Parser)
	print colored("Toplam paket sayisi : ", "green"), toplam
	print colored("Beacon      : ", "green"), beacon
	print colored("ProbeR      : ", "green"), probereq
	print colored("ProbeResp   : ", "green"), proberes
	print colored("\nSSIDList    : ", "green"), ssidlist
	print colored("\nBSSIDList   : ", "green"), bssidlist

