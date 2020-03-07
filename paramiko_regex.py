import paramiko
import time
import getpass
import re
# import xlsxwriter

data_router = open("ip_regex.txt", "r").read()

data = data_router.split("\n")

# workbook = xlsxwriter.Workbook('DataNeightbor7Maret.xlsx')
# worksheet = workbook.add_worksheet("Basic Neightbor Info")
# worksheet.write("A1", "Hostname")
# worksheet.write('B1', "FQDN")
# worksheet.write("C1", "Serial Number")
# worksheet.write("D1", "Uptime")
# worksheet.write("E1", "Vendor")

# row = 1
# col = 0

for i in range (len(data)):
    j = i+1
    ip = data[i]
    user = "cisco"
    passw = "cisco"
    print("===============================================================================================")
    print("ip: ", ip)
    print("user: ", user)
    print("password: ", passw)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=user, password=passw, allow_agent=False, look_for_keys=False)

    print("Success login to {}".format(ip))
    conn = ssh_client.invoke_shell()

    conn.send("terminal length 0\n")
    conn.send("show cdp neighbor detail\n")
    time.sleep(1)

    output = conn.recv(65535).decode()
    # print(type(output))
    # print(type(output.decode()))
    print(output)

    # IOU7 uptime is 40 minutes
    hostname_uptime = re.search(r"(.+) uptime is (.+)", output)
    print(hostname_uptime.group(0))
    hostname = hostname_uptime.group(1)
    uptime = hostname_uptime.group(2)
    print("hostname = ", hostname)
    print("uptiime = ", uptime)

    # file_ip = open(f"file_paramiko_regex{j}.txt","w")
    # file_ip.write(output.decode())

ssh_client.close()
