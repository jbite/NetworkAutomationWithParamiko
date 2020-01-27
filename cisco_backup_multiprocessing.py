import getpass
import multiprocessing as mp

import myparamiko

def backupmycisco(hostname,username,password):
    ssh_client = myparamiko.MyParamiko(hostname,22,username,password)
    ssh_client.connect()
    ssh_client.get_shell()
    ssh_client.backupcfg()
    ssh_client.close()

if __name__ == '__main__':
    username = input("Enter username: ")
    password = getpass.getpass("Password: ")
    filename = "hostlist_nw_cisco.txt"#input("Enter host file: ")

    process_list = list()

    with open(filename,'r') as f:
        hostlist = f.read().splitlines()

    for host in hostlist:
        process = mp.Process(target=backupmycisco,args=(host,username,password,))
        process_list.append(process)

    for p in process_list:
        p.start()

    for p in process_list:
        p.join()

    print('End of Script')
