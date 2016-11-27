#!/usr/bin/env python
from __future__ import print_function
import paramiko
import sys
import os

f = open('sshhosts')

hosts = f.readlines()
f.close()

username = 'root'
# password = sys.argv[1]
password = 'w'
port = 22

for host in hosts:
    scp = 'scp -r software '+host+':/root/'
    print (scp)
    os.system(scp)

    cmd = '''
        ssh root@ 'rpm -ivh /root/software/tcl-8.5.7-6.el6.x86_64.rpm'
        ssh root@%host 'rpm -ivh /root/software/expect-5.44.1.15-5.el6_4.x86_64.rpm'
    '''

    paramiko.util.log_to_file('ssh_insExpect.log')

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(host, port, username, password)
    stdin, stdout, stderr = s.exec_command(cmd)

    print(stdout.read())
    print(stderr.read())

    s.close()
