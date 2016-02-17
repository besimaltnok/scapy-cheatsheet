
### Kablosuz ağlarda sniffing


+ Kullanılabilecek kalıplar

```python
 + packets = sniff(iface='wlan0mon', prn=KablosuzAnaliz)
```


```python
pkt.type 
#(Management(0), Data(1))
```

```python
pkt.subtype
#(Beacon(8), ProbeReq(4), ProbeResp(5))
```

```python
pkt.info
#(SSID bilgisi)
```

```python
ord(pkt0[Dot11Elt:3].info)
#(Kanal numarası)
```

```python
256-(ord(pkt.notdecoded[-4:-3]))
#(Sinyal gücü)
```
