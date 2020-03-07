from napalm import get_network_driver
import json

ip = "192.168.122.46"

driver = get_network_driver("ios")
ios_r1 = driver(ip, "cisco", "cisco")
ios_r1.open()

r1_facts = ios_r1.get_facts()

# x = json.dumps(r1_facts, indent=3)

# y = json.loads(x)

print("HOSTNAME = ", r1_facts["hostname"])
print("UPTIME = ", r1_facts["uptime"])


ios_r1.close()