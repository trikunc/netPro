import paramiko
import time
import getpass
from jinja2 import Template
import yaml
import json.tool

template_file = open('./templateUser.j2',"r").read()
template = Template(template_file)

file_data = open('./user_data.yml', 'r')
data_yaml = yaml.load(file_data)
print(json.dumps(data_yaml, indent=3))

for router in data_yaml:
	ssh_client = paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh_client.connect(hostname=router['ip'],username=router['username'], password=router['password'], look_for_keys=False)

	print (f"Success login to {router['ip']}")
	conn = ssh_client.invoke_shell()

	ip_data = router.get("new_ip")
	print("new ip = ",ip_data)
	
	if ip_data is not None:
		cmds = template.render(list_users=router["new_user"], interface_list=router["new_ip"] )
	else: 
		cmds = template.render(list_users=router["new_user"])
	
	conn.send("conf t\n")
	for cmd in cmds.split("\n"):
		conn.send(cmd + "\n")
		time.sleep(1)

	output = conn.recv(65535)
	print (output.decode())

	ssh_client.close()
print("Selamat anda success !")
