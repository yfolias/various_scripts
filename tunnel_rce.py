#!/usr/bin/env python
# Yannis Folias
# Remote command execution via proxy server by using parallel-ssh
# https://parallel-ssh.readthedocs.io/en/latest/
import boto3
import sys
from pssh.clients import ParallelSSHClient

sshKey = "host_key"
proxy_user = "proxy_user"
proxyKey = "proxy_ey"
proxy_host = 'proxy_ip'
# bastion_hosts = []
host = ["host_ip"]
host_user = "host_user"

# try:
#     ec2client = boto3.client('ec2')
#     response = ec2client.describe_instances(
#         Filters=[
#             {
#                 'Name': 'tag:Name',
#                 'Values': [
#                     'test',
#                 ]
#             },
#         ])
#     for i in range(len(response)):
#         publicIps = (response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
#         bastion_hosts.append(publicIps)
# except Exception as e:
#     sys.exit(e)

try:
    proxyClient = ParallelSSHClient(host, proxy_host=proxy_host, proxy_user=proxy_user, proxy_pkey=proxyKey, proxy_port=22,  user=host_user, pkey=sshKey)
    #com = proxyClient.run_command('mysql -h [host] -u p[user] -p[pass] --execute="SHOW DATABASES;"')
    com = (f"ifconfig")
    command = proxyClient.run_command(f'{com}')
    for host, host_output in command.items():
        print(f"\n{proxy_host} \n")
        for line in host_output.stdout:
            print(line)
    proxyClient.join(command)
except Exception as e:
    print(e)

