import csv
csv_file = open('data/SSH.csv', 'a+')
df =['user','is_private','is_failure','is_root','is_valid','not_valid_count','ip_failure','ip_success','no_failure','first','td','ts','class']
writer = csv.DictWriter(csv_file, fieldnames=df)
from ssh_parse import *
up = Parse_SSH()
file = open("ssh_log_files/auth3.log")
lines = file.read().split("\n")
temp_dict = {}
for line in lines:
    if str(line).find("ssh") != -1:
        dict = up.SSHProcessed(line)
        if dict == {}:
            continue
        elif dict != temp_dict:
            print(dict)
            if int(dict['not_valid_count']) > 4 or (int(dict['ip_failure']) > (int(dict['ip_success'])+1) and int(dict['is_failure']) == 1):
                if int(dict['td']) < 100 and int(dict['first']) != 1:
                    dict.update({"class":1})
                elif int(dict['td']) < 100 and int(dict['is_valid']) == 0:
                    dict.update({"class": 1})
            else:
                dict.update({"class": 0})
            writer.writerow(dict)
            temp_dict = dict
        else:
            continue
