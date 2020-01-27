import getpass

import paramiko

hostname = input("Hostname or IP : ")
username = input("Username : ")
password = getpass.getpass("Password : ")
command = "ifconfig"
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname,port=22,username=username,password=password,look_for_keys=False,allow_agent=False)
stdin,stdout,stderr = ssh_client.exec_command(command)

output = stdout.read().decode()
print(output)
ssh_client.close()

with open('R1_show_run.txt', 'w') as f:
    f.write(output)
