#TODO pytail is required for this package
import sys
import subprocess
from pygtail import Pygtail
import time
import subprocess
import select
from  parse_ubuntu import *
auth_path = "/var/log/auth.log"

print("Initializing SSH session monitoring...")
up = ParseUbuntu()
f = subprocess.Popen(['tail','-F',auth_path],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)

p = select.poll()
p.register(f.stdout)
while True:
    if p.poll(1):
        temp = f.stdout.readline()
        temp = str(temp)
        #print(temp)
        if str(temp).find("ssh") != -1:
            if up.parsingAbort(temp) == 0:
                is_private,is_failure, is_root, is_valid, user, ip,td,nf=up.SshProcessed(temp)
                print(" \t is_failure: {0} , is_root: {1} , is_valid: {2} , user: {3} , ip: {4} ,no_failure: {5} , td: {6}, is_private:{7}".format(is_failure, is_root, is_valid, user, ip,nf,td,is_private))



    time.sleep(0.01)
#Data
#[internal,failed,td,root,root_access,attempts]
