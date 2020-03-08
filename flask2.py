from flask import  Flask, request, jsonify
import json
import paramiko
import time
import re
# import getpass #//get pasword (make hiden password)

app = Flask(__name__)

@app.route('/show_info', methods=["GET"])
def show_info():
    ip = request.args.get("ip_router")
    user = request.args.get("user")
    passw = request.args.get("passw")

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=user, password=passw, allow_agent=False, look_for_keys=False)

    conn = ssh_client.invoke_shell()
    conn.send("terminal length 0\n")
    conn.send("show cdp neighbor detail\n")
    time.sleep(1)
    output = conn.recv(65535).decode()

    hostname_src = re.findall(r"Device ID: (.+)", output)
    interface_src = re.findall(r"Interface: (.+),", output)
    outgoing_src = re.findall(r"\(outgoing port\): (.+)", output)
    ip_src = re.findall(r"IP address: (.+)", output)
    platform_src = re.findall(r"Platform: (.+),", output)

    all_neightbor = []
    for index,result in enumerate(hostname_src):
        all_neightbor.append({
            "remote_hostname": result,
            "interface": interface_src[index],
            "outgoing": outgoing_src[index],
            "ip source": ip_src[index],
            "platform": platform_src[index]
        }) 

    ssh_client.close()

    return jsonify(all_neightbor)


app.run(host='0.0.0.0', port=80, debug=True)
