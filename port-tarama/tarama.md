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

+ XMAS Scan

```python
xmas = IP(dst=dst_ip)/TCP(dport=dst_port,flags="FPU")
sr1(xmass, timeout=2)
```

+ FIN Scan

```python
fin = IP(dst=dst_ip)/TCP(dport=dst_port,flags="F")
sr1(fin, timeout=10)
```

+ NULL Scan

```python
null = IP(dst=dst_ip)/TCP(dport=dst_port,flags="")
sr1(null, timeout=10)
```

### Parametreler

+ type    = Dönen verinin tipini sorgulayabilirsiniz. ( Örnek dönen değer : type 'NoneType')
+ dport   = Hedef  port adresi
+ sport   = Kaynak port adresi
+ timeout = Cevap dönülmesi için beklenecek süre zarfı
