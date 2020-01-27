import getpass

import myparamiko

hostlist = ["10.255.0.2",
            "10.255.0.3",
            "10.255.0.5",
            "10.255.0.16",
            "10.255.0.17",
            "10.255.0.18",
            "10.255.0.21",
            "10.255.0.28",
            "10.255.0.29",
            "10.255.0.30",
            "10.255.0.31",
            "10.255.0.32",
            "10.255.0.33",
            "10.255.0.131",
            "10.255.0.132"
            ]
#input("Hostname or IP : ")
username = "jacky.feng"#input("Username : ")
password = "Ft226847494!"#getpass.getpass("Password : ")

for hostname in hostlist:
    ssh_client = myparamiko.MyParamiko(hostname,22,username,password)
    ssh_client.connect()
    ssh_client.get_shell()
    ssh_client.backupcfg()
    ssh_client.close()
