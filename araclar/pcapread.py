#!/usr/bin/env python

import sys
from scapy.all import *

pcap_path = ""
packets   = rdpcap(pcap_path)

for pkt in packets:
   # Do something
