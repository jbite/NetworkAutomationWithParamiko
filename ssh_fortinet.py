import paramiko
import time

time.sleep(1)

ip = "10.255.0.18"
host = ip
username = "admin"
password = "p@ssword,123"

remote_conn_pre = paramiko.SSHClient()
#remote_conn_pre
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
print("SSH connection established to " + host)

remote_conn = remote_conn_pre.invoke_shell()
print("Interactive SSH session established")

output = remote_conn.recv(1000)
print(output.decode())

while True:
    cmd = input('>>:')
    remote_conn.send(cmd+'\n')
    time.sleep(1)
# time.sleep(0.5)
# remote_conn.send('p@ssword,123\n')
# time.sleep(0.5)
# remote_conn.send('\n')
# time.sleep(1)
# remote_conn.send('show vlan br \n')
# time.sleep(2)
    print(remote_conn.recv(65535).decode())
# if output[-9:] in '--More--':
#     remote_conn.send(' ')
#     time.sleep(1)
#     output = remote_conn.recv(65535).decode()
#     print(output)