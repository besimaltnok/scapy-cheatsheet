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
icmp.type = echo-request
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

* DHCP 
