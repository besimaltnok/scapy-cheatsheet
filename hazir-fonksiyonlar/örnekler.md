### Scapy içerisinde hazır larak gelen fonksiyonlar

+ Wireshark

```python
arp = ARP()
wireshark(arp)
```

+ Traceroute

```python
traceroute(["www.canyoupwn.me"],maxttl=20)
```

+ Promiscping

```python
promiscping("192.168.2.0/24")
```

+ ARPing

```python
arping("192.168.2.0/24")
```
