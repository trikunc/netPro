from napalm import get_network_driver
from pprint import pprint
import xlsxwriter

ip_list = ["192.168.122.12", "192.168.122.192","192.168.122.85","192.168.122.158"]

workbook = xlsxwriter.Workbook('DataRouter1Maret.xlsx')
worksheet = workbook.add_worksheet("Basic Router Info")
worksheet.write("A1", "Hostname")
worksheet.write('B1', "FQDN")
worksheet.write("C1", "Serial Number")
worksheet.write("D1", "Uptime")
worksheet.write("E1", "Vendor")

row = 1
col = 0

for ip in ip_list:
    print("connecting to ", ip)
    driver = get_network_driver("ios")
    ios_r1 = driver(ip,"cisco","cisco")
    ios_r1.open()
    
    r1_facts = ios_r1.get_facts()

    hostname = r1_facts["hostname"]
    fqdn = r1_facts['fqdn']
    serial_number = r1_facts['serial_number']
    uptime = r1_facts["uptime"]
    vendor = r1_facts["vendor"]

    worksheet.write(row, col, hostname)
    worksheet.write(row, col+1, fqdn)
    worksheet.write(row, col+2, serial_number)
    worksheet.write(row, col+3, uptime)
    worksheet.write(row, col+4, vendor)
    row = row + 1

    ios_r1.close()

workbook.close()
