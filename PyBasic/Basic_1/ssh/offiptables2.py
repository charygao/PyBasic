#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pexpect

print("请输入密码，每台机器的密码应保持一致：")
cmd = "service iptables stop"
passwd = raw_input()

def ssh_cmd(passwd, cmd):
    ret = -1
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            ssh = pexpect.spawn('ssh root@%s "%s"' % (line, cmd))
            try:

                i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=2)
                if i == 0:
                    ssh.sendline(passwd)
                elif i == 1:
                    ssh.sendline('yes\n')
                    ssh.expect('password: ')
                    ssh.sendline(passwd)
                    ssh.sendline(cmd)
                    r = ssh.read()
                    print(r)
                    ret = 0
            except pexpect.EOF:
                print("EOF")
                ssh.close()
                ret = -1
            except pexpect.TIMEOUT:
                print("TIMEOUT")
                ssh.close()
                ret = -2
            return ret
