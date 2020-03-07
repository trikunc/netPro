import paramiko
import time
import getpass

data_router = open("ip.txt", "r").read()

data = data_router.split("\n")

for i in range (len(data)):
    j = i+1
    ip = data[i]
    user = "admin"
    passw = "Tselnss0"
    print("===============================================================================================")
    print("ip: ", ip)
    print("user: ", user)
    print("password: ", passw)

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=user, password=passw, allow_agent=False, look_for_keys=False)

    print("Success login to {}".format(ip))
    conn = ssh_client.invoke_shell()

    # conn.send("terminal length 0\n")
    conn.send("ip interfaces show\n")
    # conn.send("show interfaces summary\n")
    time.sleep(10)

    output = conn.recv(65535)
    # print(type(output))
    # print(type(output.decode()))
    # print(output.decode())

    file_ip = open(f"file_paramiko{j}.txt","w")
    file_ip.write(output.decode())

ssh_client.close()
