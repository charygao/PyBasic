#!/usr/bin/env python
from __future__ import print_function
import paramiko
import sys

f = open('sshhosts')

hosts = f.readlines()
f.close()

username = 'root'
password = sys.argv[1]
port = 22

for host in hosts:
    cmd = 'service iptables status'
    paramiko.util.log_to_file('ssh_StopIpTables.log')

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(host, port, username, password)
    stdin, stdout, stderr = s.exec_command(cmd)

    print(stdout.read())
    print(stderr.read())

    s.close()
