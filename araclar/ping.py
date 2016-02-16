#!/usr/bin/env python
# -*- coding : urf-8 -*-

from scapy.all import *

packet = IP(dst='ip_for_ping') / ICMP()
sr1(packet)
