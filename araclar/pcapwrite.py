#!/usr/bin/env python

import sys
from scapy.all import *

def PcapWrite(pkt):
   # Do something
   wrpcap("pcap_name", pkt)

if __name__ == "__main__":
   sniff(iface = 'wlan0', count=5, prn=PcapWrite)
