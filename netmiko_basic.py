from netmiko import ConnectHandler

data_router = open("ip.txt", "r").read()

data = data_router.split("\n")

for i in range (len(data)):
    ip = data[i]
    # print(ip)
    router = {
        "device_type" : "cisco_ios",
        "ip" : ip,
        "username" : "cisco",
        "password" : "cisco"
    }

    conn = ConnectHandler(**router)
    print(f"==================================================={i}================================================================")
    for j in range (200, 211):
        # print(i)
        cmds = []
        cmds.append(f'interface lo{j}')
        cmds.append(f'ip address {j}.1.1.1 255.255.255.255')
        cmds.append('description from netmiko')
    # print(conn.send_config_set(cmds))
    print(conn.send_command("show ip int br | i up"))