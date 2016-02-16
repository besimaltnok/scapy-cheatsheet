### Scapy ile port tarama örnekleri

+ SYN Scan

```python
syn = IP(dst="72.14.207.99")/TCP(dport=80,flags="S")
sr1(syn)
```

+ ACK Scan

```python
ack = IP(dst="72.14.207.99")/TCP(dport=80,flags="A")
sr1(syn)
```
