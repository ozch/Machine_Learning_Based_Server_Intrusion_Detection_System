import csv
csv_file = open('data/SSH.csv', 'a+')
df =['is_private', 'is_failure', 'is_root', 'is_valid', 'user', 'ip_failure','ip_success','no_failure','td','first','ts','class']
writer = csv.DictWriter(csv_file, fieldnames=df)
from ssh_parse import *
up = Parse_SSH()
file = open("auth2.log")
lines = file.read().split("\n")
temp_dict = {}
for line in lines:
    if str(line).find("ssh") != -1:
        dict = up.SSHProcessed(line)
        if dict == {}:
            continue
        elif dict != temp_dict:
            print(dict)
            writer.writerow(dict)
            temp_dict = dict
        else:
            continue
