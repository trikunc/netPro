# pip install napalm
from napalm import get_network_driver
import json
import xlsxwriter

ip_list = ["192.168.122.12", "192.168.122.192","192.168.122.85","192.168.122.158"]

workbook = xlsxwriter.Workbook('DataRouterInterface1Maret-2.xlsx')

worksheet = workbook.add_worksheet("Interface Info")

worksheet.write("A1", "IP Address Router")
worksheet.write('B1', "Interface Name")
worksheet.write("C1", "Status")
worksheet.write("D1", "Description")
worksheet.write("E1", "MAC Address")

row = 1
col = 0

for ip in ip_list:
	print(f"Extract interface info on {ip}")
	
	# Konek ke napalm
	driver = get_network_driver("ios")
	ios_r1 = driver(ip,"cisco","cisco")
	ios_r1.open()

	# get interface info dari router
	r1_interfaces = ios_r1.get_interfaces()
	# print(json.dumps(r1_facts, indent=3))
	
	worksheet.write(row, col, ip)

	for interface,data in r1_interfaces.items():
	    status = data["is_up"]
	    deskripsi = data["description"]
	    mac_address = data["mac_address"]
		
	    worksheet.write(row, col+1, interface)
	    worksheet.write(row, col+2, status)
	    worksheet.write(row, col+3, deskripsi)
	    worksheet.write(row, col+4, mac_address)
	    row = row + 1

	ios_r1.close()

workbook.close()
# print hostname dan uptime nya aja

