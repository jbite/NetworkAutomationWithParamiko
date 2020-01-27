import getpass
import time

import paramiko

hostname = "10.255.0.18"#input("Hostname or IP : ")
username = "jacky.feng"#input("Username : ")
password = "Ft226847494!"#getpass.getpass("Password : ")
command = "ifconfig"
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname,port=22,username=username,password=password,look_for_keys=False,allow_agent=False)

remote_connection = ssh_client.invoke_shell()
# remote_connection.send('conf t\n')
# remote_connection.send('vlan 1111\n')
# remote_connection.send('name VLAN_paramiko\n')
# remote_connection.send('end\n')
remote_connection.send('terminal length 0\n')
remote_connection.send('show vlan br\n')
time.sleep(3)
output = remote_connection.recv(4096)
print(output.decode())
# print(type(remote_connection))
ssh_client.close()

# with open('R1_show_run.txt', 'w') as f:
    # f.write(output)
