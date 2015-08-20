#!/usr/bin/python
#coding=utf-8

from fabric.api import env, run
from fabric.contrib.files import append
import config
import datetime
import os
import socket

LOCAL_PUBKEY_FILE = os.path.expanduser('~') + '/.ssh/' + 'id_rsa.pub'

def get_hosts():
    hosts = {}
    for addr in config.HOSTS:
        if ':' in addr:
            ip,port = addr.split(":")
        else:
            ip = addr
            port = config.DEFAULT_SSH_PORT
        port = int(port)
        hosts[ip] = "%s:%s"%(ip,port)
    return hosts


hosts = get_hosts()
env.hosts = list(set(hosts.values()))
env.user = config.USER
env.password = config.PASSWORD

def nopassword(**ip_list):
    host = env.host_string
    if len(ip_list) > 0 and host not in env.hosts:
        return

    now = datetime.datetime.now()
    tmp_key_file = now.strftime("ssh_%Y-%m-%d_%H-%M-%S")

    #print "os.pwd: %s %s" % (os.getcwd(), socket.gethostname())
    if not os.path.isfile(LOCAL_PUBKEY_FILE):
        print "pubkey file %s does not exist" %(LOCAL_PUBKEY_FILE )
        return

    pubkey = open(LOCAL_PUBKEY_FILE).readline()
    run('mkdir -p ~/.ssh')
    append('~/.ssh/authorized_keys', pubkey, partial = False)
    run('chmod 600 ~/.ssh/authorized_keys')
    run('chmod 700 ~/.ssh')

