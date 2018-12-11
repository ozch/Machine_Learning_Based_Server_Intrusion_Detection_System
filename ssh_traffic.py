#TODO pytail is required for this package
import sys
import subprocess
from pygtail import Pygtail
import time
import subprocess
import select

auth_path = "/var/log/auth.log"
#subprocess.call(['chmod', '-R', '+w', auth_path])
print("Initializing SSH session monitoring...")
#for line in Pygtail(auth_path):
#    sys.stdout.write(line)
#    print("---")


f = subprocess.Popen(['tail','-F',auth_path],\
        stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)


while True:
    if p.poll(1):
        temp = f.stdout.readline()
        temp = str(temp)
        print(temp)
        if str(temp).find("ssh") != -1:
            if parsingAbort(temp) == 0:
                is_failure, is_root, is_valid, user, ip=SHHConnections(temp)
                if user != "-1" or ip != "-1":
                    print(" \t is_Failure: {0} , is_Root: {1} , is_Valid: {2} , User: {3} , IP: {4} ".format(is_failure, is_root, is_valid, user, ip))



    time.sleep(0.01)
#Data
#[internal,failed,td,root,root_access,attempts]
