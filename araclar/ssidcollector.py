# CanYouPwnMe

import os
import time
from scapy.all import *
from termcolor import colored

ssidlist  = []
bssidlist = []

iface = 'wlan0'

def SSIDCollector(pkt):
	if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeReq) or pkt.haslayer(Dot11ProbeResp):
		ssid = pkt.info
		mac  = pkt.addr2
		if mac not in bssidlist:
			if '\x00' in ssid:
				ssidlist.append('Gizli SSID-'+mac)
				bssidlist.append(mac)
			else:
				bssidlist.append(mac)
				ssidlist.append(ssid)


def ChannelHop():

	for channel in range(1, 14):
		os.system("iwconfig " + iface + " channel " + str(channel))
		print "[+] Sniffing on channel " + str(channel)

		sniff(iface=iface, prn=SSIDCollector, count=20, timeout=5)
		
if __name__ == '__main__':
	os.system('reset')
	print colored("Channel Hopping started for SSID Collector", "green")
	ChannelHop()
	time.sleep(3)
	os.system('reset')
	print colored("SSID List :\n", "green")
	print ssidlist

	
