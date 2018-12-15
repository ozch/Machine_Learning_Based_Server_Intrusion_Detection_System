import ipaddress
import time
import re
class Parse_SSH:
    dict = {}
    number_of_failure = 0

    def GetFailure(self):
        return self.number_of_failure

    def ParseUsr(self,line):
        usr = None
        flag = 0
        if "Accepted password" in line:
            usr = re.search(r'(\bfor\s)(\w+)', line)
        elif "sudo:" in line:
            usr = re.search(r'(sudo:\s+)(\w+)', line)
        elif "authentication failure" in line:
            usr = re.search(r'USER=\w+', line)
        elif "for invalid user" in line:
            usr = re.search(r'(\buser\s)(\w+)', line)
        elif "Invalid user" in line:
            flag = 1
            str_ = line
            loc_start = str_.find("Invalid user ") + len("Invalid user ")
            loc_end = str_.find(" from")
            usr = str_[loc_start:loc_end]
        if usr is not None:
            if flag == 1:
                return usr
            return usr.group(2)
        else:
            return "-1"
    # parse an IP from a line
    def ParseIP(self,line):
        ip = re.search(r'(\bfrom\s)(\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b)', line)
        if ip is not None:
            return ip.group(2)
        else:
            ip = "-1"
            return ip
    def isPrivate(self,ip):
        try:
            is_private = int(ipaddress.ip_address(ip).is_private)
            return is_private
        except:
            return 0
    # parse a date from the line
    def ParseDate(self,line):
        date = re.search(r'^[A-Za-z]{3}\s*[0-9]{1,2}\s[0-9]{1,2}:[0-9]{2}:[0-9]{2}', line)
        if date is not None:
            print("Date " + str(date))
            return date.group(2)
        else:
            "-1"

    # parse a command from a line
    def ParseCmd(line):
        # parse command to end of line
        cmd = re.search(r'(\bCOMMAND=)(.+?$)', line)
        if cmd is not None:
            return cmd.group(2)
    def isRoot(self,line):
        if line.find("root") != -1:
            return 1
        else:
            return 0
    def SSHProcessed(self,line):
        t = time.time()
        # match a login
        if "Invalid user" in line:
            usr = self.ParseUsr(line)
            ip = self.ParseIP(line)
            is_private = self.isPrivate(ip)
            self.number_of_failure= self.number_of_failure+1
            is_failure = "1"
            is_root = self.isRoot(line)
            is_valid = "0"
        elif "Accepted password for" in line:
            usr = self.ParseUsr(line)
            ip = self.ParseIP(line)
            is_private = self.isPrivate(ip)
            self.number_of_failure=0
            is_failure = "0"
            is_root = self.isRoot(line)
            is_valid = "1"
        # match a failed login
        elif "Failed password for" in line:
            usr = self.ParseUsr(line)
            ip = self.ParseIP(line)
            is_private = self.isPrivate(ip)
            self.number_of_failure = self.number_of_failure + 1
            is_failure = "1"
            is_root = self.isRoot(line)
            is_valid = 0

        elif "authentication failure;" in line:
            usr = self.ParseUsr(line)
            ip = self.ParseIP(line)
            is_private = self.isPrivate(ip)
            self.number_of_failure = self.number_of_failure + 1

            is_failure = "0"
            is_root = self.isRoot(line)
            is_valid = 0
        else:
            usr = "-1"
            ip = "-1"
            return {}
        print("IP ADDRESS : " + ip)

        print("IS ROOT : " + str(is_root))
        print("IS VALID: " + str(is_valid))
        print("IS FAILURE: " + str(is_failure))
        print("IS PRIVATE: " + str(is_private))
        if usr != "-1" or ip != "-1":
            if self.dict.get(ip) == None:
                if is_failure == "0":
                    self.dict.update({ip: {"is_private": is_private, "is_failure": is_failure, "is_root": is_root,"is_valid": is_valid, "user": usr,"ip_failure":0,"ip_success":1, "no_failure": self.number_of_failure, "td": int(t)}})
                else:
                    self.dict.update({ip: {"is_private": is_private, "is_failure": is_failure, "is_root": is_root,"is_valid": is_valid, "user": usr,"ip_failure":1,"ip_success":0, "no_failure": self.number_of_failure, "td": int(t)}})

            else:
                t_old = self.dict[ip]["td"]

                if is_failure == "0":
                    self.dict[ip]["ip_success"] = self.dict[ip]["ip_success"] +1
                    self.dict.update({ip: {"is_private": is_private, "is_failure": is_failure, "is_root": is_root,"is_valid": is_valid, "user": usr,"ip_failure":0,"ip_success":1, "no_failure": self.number_of_failure, "td": int(t)}})
                else:
                    self.dict[ip]["ip_failure"] = self.dict[ip]["ip_failure"] + 1
                    self.dict.update({ip: {"is_private": is_private, "is_failure": is_failure, "is_root": is_root,"is_valid": is_valid, "user": usr,"ip_failure":1,"ip_success":0, "no_failure": self.number_of_failure, "td": int(t)}})
        if self.dict.get(ip) == None:
            return {}
        return self.dict[ip]


        # match commands
        #elif "sudo:" in line:
        #    # parse user
        #    usr = self.ParseUsr(line)


        #    cmd = self.ParseCmd(line)
        #    # append the command if it isn't there already
        #    if cmd is not None:
        #        if not cmd in logs[usr].commands:
        #            logs[usr].commands.append(cmd)
        #    logs[usr].logs.append(line.rstrip('\n'))