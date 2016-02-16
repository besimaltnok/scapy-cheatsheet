### İstediğimiz içerikte paketler üretmek

* TCP

```python
tcp = TCP()
tcp.show()
tcp.display()
tcp.dport = 80
```

* ICMP

```python
icmp = ICMP()
icmp.show()
icmp.display()
icmp.type = "echo-request"
```

* IP

```python
ip = IP()
ip.show()
ip.display()
ip.src = RandSort()
```

* ARP

```python
arp = ARP()
arp.show()
arp.display()
arp.hwsrc = RandMAC()
```

* UDP

```python
udp = UDP()
udp.show()
udp.display()
udp.dport = 53
```

* DNS

```python
dns  = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname="www.thepacketgeek.com"))
a, un = sr1(dns, verbose=0)
print a[DNS].summary()
```

* DHCP 

```python
dhcp = DHCP() / BOOTP()
dhcp.show()
dhcp.display()
dhcp[BOOTP].op = "BOOTREQUEST"
dhcp[BOOTP].giaddr = "gateway_ip_address"
```
