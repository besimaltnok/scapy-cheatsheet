#!/usr/bin/env python

import sys
from scapy.all import *

syn = (IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)

sr1(syn)
