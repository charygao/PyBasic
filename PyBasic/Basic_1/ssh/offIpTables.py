# coding=utf-8

"""
这种方式只适用于成熟的服务器中
因为缺包太严重
"""

from __future__ import print_function
from fabric.api import cd, run, env, hosts
from fabric.decorators import parallel

f = open('sshhosts')
env.hosts = f.readlines()
f.close()

env.port = 22
env.password = 'w'


@parallel(pool_size=5)
def offIpTables():
    run("service iptables status")
