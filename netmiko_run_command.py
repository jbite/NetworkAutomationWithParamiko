from netmiko import Netmiko
from netmiko import ConnectHandler
# connection = Netmiko(host='10.255.0.18',username='jacky.feng',password='Ft226847494!',device_type='cisco_ios')
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '10.255.0.18',
    'username': 'jacky.feng',
    'password': 'Ft226847494!',
    'port': 22,
    'secret': None,
    'verbose':True
}

connection = ConnectHandler(**cisco_device)
prompt = connection.find_prompt()
print(prompt)
if '>' in prompt:
    connection.enable()


output = connection.send_command('sh ip inter br')
# print(output)

mode = connection.check_config_mode()
# print(mode)
connection.disconnect()
