import pymysql

sqlconn = pymysql.connect('192.168.100.87','root','ubuntu','netprog')

cursor = sqlconn.cursor(pymysql.cursors.DictCursor)

ip_address = "192.168.122.113"
username = "cisco"
password = "cisco"

cursor.execute("INSERT INTO Devices(ip_address, username, password) VALUES ('{}','{}','{}')".format(ip_address, username, password))

sqlconn.commit()

cursor.execute("SELECT * FROM Devices3")

data = cursor.fetchall()

from pprint import pprint
pprint(data)
