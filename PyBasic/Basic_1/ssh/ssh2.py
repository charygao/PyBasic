# coding=utf-8
from __future__ import print_function
from fabric.api import hosts, env
from fabric.operations import run, local

f = open('/home/lele/文档/Codes/Pycharm/PyBasic/PyBasic/PyBasic/Basic_1/ssh/sshhosts', 'r')
env.hosts = f.readlines()
f.close()

env.password = 'wangle'

run('ls -l')
