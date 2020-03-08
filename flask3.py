from flask import  Flask, request, jsonify
import json
import paramiko
import time
import re
# import getpass #//get pasword (make hiden password)

app = Flask(__name__)

def connect(ip_mgmt, user, passw):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_mgmt, username=user, password=passw, allow_agent=False, look_for_keys=False)

    conn = ssh_client.invoke_shell()

    return conn

@app.route('/config_int', methods=["POST"])
def show_info():
    data = request.get_json()

    ip_mgmt = data["ip"]
    user = data["user"]
    passw = data["passw"]
    new_intx =data["new_int"]


    conn = connect(ip_mgmt, user, passw)
    conn.send("conf t\n")

    for index, newint in enumerate(new_intx):
        new_int = newint["new_int2"]
        int_desc = newint["int_desc"]
        new_ip = newint["new_ip"]
        conn.send(f"int {new_int}\n")
        conn.send(f"desc {int_desc}\n")
        conn.send(f"ip address {new_ip}\n")
        time.sleep(1)


    output = conn.recv(65535).decode()

    data = {
        "result": output
    }

    return jsonify(data)
app.run(host='0.0.0.0', port=80, debug=True)
