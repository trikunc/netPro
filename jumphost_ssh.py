# Dependency = pip install jumpssh
# Documentation = https://pypi.org/project/jumpssh/

# import xlsxwriter
from jumpssh import SSHSession

# workbook = xlsxwriter.Workbook('jumphost_ssh_8Maret.xlsx')
# worksheet = workbook.add_worksheet("Basic Router Info")
# worksheet.write("A1", "Interface")
# worksheet.write('B1', "IP-Address")
# worksheet.write("C1", "Ok?")
# worksheet.write("D1", "Method")
# worksheet.write("E1", "Status up")
# worksheet.write("F1", "Protocol up")

# row = 1
# col = 0

gateway_session = SSHSession(host="192.168.100.4",username="netprog",password="netprog").open()

ip_list = ["192.168.122.226", "192.168.122.119"]

for ip in ip_list:
    print("connecting to ", ip)
    remote_session = gateway_session.get_remote_session(ip, username="cisco", password="cisco", look_for_keys=False)
    print(remote_session.get_cmd_output("sho ip int br"))
    print(remote_session.get_cmd_output("sho version | i uptime"))
    print("=========================================================================================")
    print("\n")



