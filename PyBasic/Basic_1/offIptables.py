#!/usr/bin/python
from __future__ import print_function
import paramiko
import threading


def ssh2(ip, username, passwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, username, passwd, timeout=5)
    for m in cmd:
        stdin, stdout, stderr = ssh.exec_command(m)
        out = stdout.read(),
        for o in out:
            if not o:
                print("error %s" % ip)
                break
            print(o)
            print('%s\tOK\n' % (ip))
    ssh.close()


if __name__ == '__main__':
    cmd = ['service iptables status']
    username = "root"
    passwd = "123456"
    threads = [4]
    file = open("sshhosts")
    f = file.read().split()
    for ip in f:
        a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
        a.start()
    print("current has %d threads" % (threading.activeCount() - 1))
