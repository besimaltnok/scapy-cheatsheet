#!/usr/bin/env python
# -*- coding : urf-8 -*-

from scapy.all import *

ip   = IP(dst='ip_for_ping') 
icmp = ICMP()

packet = ip/icmp
sr1(packet)
