# pip install napalm
from napalm import get_network_driver
import json

ip = "192.168.122.46"

driver = get_network_driver("ios")
ios_r1 = driver(ip,"cisco","cisco")
ios_r1.open()

r1_facts = ios_r1.get_facts()

r1_interfaces = ios_r1.get_interfaces()

print(json.dumps(r1_facts, indent=3))


# for interface,data in r1_interfaces.items():
#     status = data["is_up"]
#     deskripsi = data["description"]
#     mac_address = data["mac_address"]

#     # print("\n")


# ios_r1.close()


