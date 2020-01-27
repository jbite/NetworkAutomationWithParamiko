import time
import datetime

import paramiko

class MyParamiko(object):
    def __init__(self,server_ip,server_port,user,pswd):
        self.server_ip = server_ip
        self.server_port = server_port
        self.user = user
        self.pswd = pswd
        self.ssh_client = paramiko.SSHClient()

    def connect(self):
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection = self.ssh_client.connect(self.server_ip,
                                        port=self.server_port,
                                        username=self.user,
                                        password=self.pswd,
                                        look_for_keys=False,
                                        allow_agent=False
                                        )

    def get_shell(self):
        self.connection = self.ssh_client.invoke_shell()

    def send_command(self,command,wait_time=2):
        self.connection.send(command + "\n")
        time.sleep(wait_time)
        output = ""
        while True:
            new_output = self.connection.recv(1024).decode()
            # self.connection.send('\n')
            if new_output[-1] not in ['#','>','$']:
                output = output + new_output
            else:
                output = output + new_output
                break

        return output

    def backupcfg(self):
        self.send_command("terminal length 0",wait_time=1)
        output = self.send_command("show run",wait_time=4)
        config = output.split("\n")
        config = config[4:-1]
        config = '\n'.join(config)
        print(config)
        with open('config-%s-%s.txt' % (self.server_ip,datetime.datetime.now().strftime('%Y-%m-%d')),'w') as f:
            f.write(config)

    def is_exec_mode(self):
        self.connection.send("\n")
        output = self.connection.recv(1024)
        if output.decode()[-1] == "#":
            return True
        else:
            return False

    def reactive_mode(self):
        endprompt = "[leave]"
        print("escape is %s" % endprompt)
        print("reactive mode starting")
        print('Login as user "%s"' % self.user)
        self.connection.send('\n')
        time.sleep(0.5)
        self.connection.recv(1024)
        self.connection.send("terminal length 0\n")
        time.sleep(0.5)
        self.connection.recv(1024)
        while True:
            self.connection.send("\n")
            time.sleep(0.5)
            prompt = self.connection.recv(1024)
            # print("prompt is : " + prompt.decode())
            command = input(prompt.decode())
            if command != endprompt:
                self.connection.send(command + '\n')
                time.sleep(2)
                output = ""
                while True:
                    new_output = self.connection.recv(1024)
                    # print(new_output.decode())
                    # self.connection.send("\n")
                    if new_output.decode()[-1] in ['#','$','>']:
                        break
                    else:
                        output += new_output.decode()

                print(output)
            else:
                break

    def close(self):
        self.ssh_client.close()
