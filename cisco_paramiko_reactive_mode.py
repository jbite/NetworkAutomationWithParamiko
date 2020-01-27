import getpass

import myparamiko

hostname = "10.255.0.18"#input("Hostname or IP : ")
port = 22
username = "jacky.feng"#input("Username : ")
password = "Ft226847494!"#getpass.getpass("Password : ")
command = "ifconfig"

ssh_client = myparamiko.MyParamiko(hostname,port,username,password)
ssh_client.connect()
ssh_client.get_shell()
ssh_client.send_command('terminal length 0')
output = ssh_client.send_command('show run')
print(output)
ssh_client.close()

# with open('R1_show_run.txt', 'w') as f:
    # f.write(output)
