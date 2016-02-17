### Oluşturduğumuz ve yakaladığımız paketler ile işlem yapmak


+ Liste elemanı gibi işlem görürler

```python
packets = sniff(count=7)
for pkt in packets:
   #Do something
```

+ Yakalanan paketlerin özeti

```python
packets = sniff(count=7)
packet.summary()
```

+ Yakalanan paketlerin paket numrası ile özeti

```python
packets = sniff(count=7)
packet.nsummary()
```

+ Paket elemanlarına erişmek (3. pakete erişeceğiz)

```python
packets = sniff(count=7)
pkt = packets[2]
```
