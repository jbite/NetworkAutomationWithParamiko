import getpass

import myparamiko

hostname = "10.18.1.180"#input("Hostname or IP : ")
username = "root"#input("Username : ")
password = "NewC0ast1+"#getpass.getpass("Password : ")
# command = "ifconfig"

ssh_client = myparamiko.MyParamiko(hostname,22,username,password)
ssh_client.connect()
ssh_client.get_shell()
ssh_client.send_command("useradd -m -d /home/user1 -s /bin/bash user1")
useradd = ssh_client.send_command("cat /etc/passwd")
print(useradd)

ssh_client.close()

# with open('R1_show_run.txt', 'w') as f:
    # f.write(output)
