from scapy.all import *

iface    = 'wlan1'
maclist  = []
ssidlist = []
def ProbeReqAnaliz(pkt):
        if pkt.haslayer(Dot11ProbeReq):
                ssid = pkt.info
                mac  = pkt.addr2
                if mac not in maclist and len(ssid) != 0:
                        maclist.append(mac)
                        ssidlist.append(ssid)
                        print "%s Send to %s Network Probe Request" %(mac, ssid)
                else:
                        if ssid not in ssidlist and len(ssid) != 0:
                                ssidlist.append(ssid)
                                print "%s Send to %s Network Probe Request" %(mac, ssid)

sniff(iface=iface, count=0, prn=ProbeReqAnaliz)
