### Scapy ile port tarama örnekleri

+ SYN Scan

```python
syn = IP(dst="72.14.207.x")/TCP(dport=80,flags="S")
sr1(syn)
```

+ ACK Scan

```python
ack = IP(dst="72.14.207.x")/TCP(dport=80,flags="A")
sr1(ack)
```

+ UDP Scan

```python
udp = IP(dst="192.168.1.x")/UDP(dport=[443,666])
sr(udp)
```
