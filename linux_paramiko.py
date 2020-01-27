import getpass

import paramiko

hostname = "10.18.1.180"#input("Hostname or IP : ")
username = "root"#input("Username : ")
password = "NewC0ast1+"#getpass.getpass("Password : ")
command = "yum update -y && yum install nmap -y"
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname,port=22,username=username,password=password,look_for_keys=False,allow_agent=False)
stdin,stdout,stderr = ssh_client.exec_command(command)

output = stdout.read().decode()
print(output)
ssh_client.close()

with open('%s_linuxcommand.txt' % (hostname), 'w') as f:
    f.write(output)
