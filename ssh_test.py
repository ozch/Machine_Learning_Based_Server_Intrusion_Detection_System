from ssh_parse import *
up = Parse_SSH()
file = open("auth.log")
lines = file.read().split("\n")
temp_dict = {}
for line in lines:
    if str(line).find("ssh") != -1:
        dict = up.SSHProcessed(line)
        if dict == {}:
            continue
        elif dict != temp_dict:
            print(dict)
            temp_dict = dict
        else:
            continue
