import paramiko
import time
import getpass
import re
import xlsxwriter

data_router = open("ip_regex.txt", "r").read()

data = data_router.split("\n")

workbook = xlsxwriter.Workbook('DataNeightbor7Maret.xlsx')
worksheet = workbook.add_worksheet("Basic Neightbor Info")
worksheet.write("A1", "Local Hostname")
worksheet.write('B1', "Hostname Neightbor")
worksheet.write("C1", "Interface")
worksheet.write("D1", "Outgoing")
worksheet.write("E1", "IP")
worksheet.write("F1", "Platform")

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
    # print(output)

    #     uptime = hostname_uptime.group(2)

    local_hostname_src = re.search(r"(.+)\#", output).group(1)
    print(local_hostname_src)

    hostname_src = re.findall(r"Device ID: (.+)", output)
    print(hostname_src)
    
    interface_src = re.findall(r"Interface: (.+),", output)
    print(interface_src)

    outgoing_src = re.findall(r"\(outgoing port\): (.+)", output)
    print(outgoing_src)

    ip_src = re.findall(r"IP address: (.+)", output)
    print(ip_src)

    platform_src = re.findall(r"Platform: (.+),", output)
    print(platform_src)

    print("===========================================================================================================================")

    row = 1
    col = 0
    for index,result in enumerate(hostname_src):
        worksheet.write(row, col, local_hostname_src.strip())
        worksheet.write(row, col+1, result.strip())
        worksheet.write(row, col+2, interface_src[index].strip())
        worksheet.write(row, col+3, outgoing_src[index].strip())
        worksheet.write(row, col+4, ip_src[index].strip())
        worksheet.write(row, col+5, platform_src[index].strip())
        row = row + 1
    workbook.close()




    # file_ip = open(f"file_paramiko_regex{j}.txt","w")
    # file_ip.write(output.decode())

ssh_client.close()
