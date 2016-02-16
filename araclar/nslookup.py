#!/usr/bin/env python

import sys
from scapy.all import *

host  = sys.argv[1]
cevap = sr1(IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=host)),verbose=0)
print cevap[DNSRR].rdata
