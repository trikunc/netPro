from netmiko import ConnectHandler
import netmiko
import paramiko

def fungsi(device_type, ip, user, password):
	router = {
		"device_type" : device_type,
		"ip" : ip,
		"username" : user,
		"password" : password
		}

	conn = ConnectHandler(**router)
	print (conn.send_command("show clock"))

ip_list = open("ip.txt","r").readlines()

for ip in ip_list:
	ip = ip.strip()
	print(f"Showing in {ip}")
	
	# coba ssh
	try:
		fungsi("cisco_ios", ip, "cisco", "cisco")

	except netmiko.ssh_exception.NetMikoAuthenticationException:
		print(f"{ip} berganti ke password lain ")
		fungsi("cisco_ios", ip, "cisco2", "cisco2")
	
	# kalau ssh tidak aktif, ganti ke telnet
	except paramiko.ssh_exception.SSHException:
		try:
			print(f"{ip} berganti ke telnet")
			fungsi("cisco_ios_telnet", ip, "cisco", "cisco")

		except netmiko.ssh_exception.NetMikoAuthenticationException:
			print(f"{ip} berganti ke password lain ")
			fungsi("cisco_ios_telnet", ip, "cisco2", "cisco2")


