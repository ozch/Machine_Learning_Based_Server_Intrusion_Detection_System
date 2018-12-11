class ParseUbuntu:
    # [internal,failed,td,root,root_access,attempts]
    # dict = { IP:{internal:"",root:"",failure,td,}}
    def parsingAbort(self,str_):
        if str_.find("Server listening") != -1:
            return 1
        if str_.find("disconnect") != -1:
            return 1
        if str_.find("Received disconnect") != -1:
            return 1
        if str_.find("Removed session") != -1:
            return 1
        if str_.find("New session") != -1:
            return 1
        if str_.find("Disconnected from user") != -1:
            return 1
        if str_.find("session closed") != -1:
            return 1
        if str_.find("disconnected by user") != -1:
            return 1
        if str_.find("Connection closed") != -1:
            return 1
        return 0

    def getInfoAccepted(self,str_):
        if str_.find("Accepted password for") != -1:
            loc_start = str_.find("from ") + len("from ")
            loc_end = str_.find("port")
            return str_[loc_start:loc_end - 1]
        else:
            return "-1"

    def GetFailedPasswordIP(self,str_):
        if str_.find("Failed password for ") != -1:
            loc_start = str_.find("from ") + len("from ")
            loc_end = str_.find("port")
            return str_[loc_start + 1:loc_end - 1]
        else:
            return "-1"

    def GetFirstFailedPasswordIP(self,str_):
        if str_.find("authentication failure;") != -1:
            loc_start = str_.find(" rhost=") + len(" rhost=")
            loc_end = str_.find("  user=")
            return str_[loc_start:loc_end]
        else:
            return "-1"

    def SshMonitor(self,str_):
        is_failure = 1
        is_valid = 1
        ip = ""
        ip = self.GetFirstFailedPasswordIP(str_)
        if ip == "-1":
            ip = self.GetFailedPasswordIP(str_)
            if ip == "-1":
                ip = self.getInfoAccepted(str_)
                if ip == "-1":
                    ip = "-1"
                    return 0, 0, 0, "-1", "-1"
        if str_.find("authentication failure;") != -1:
            loc_start = str_.find(" user=") + len(" user=")
            loc_end = str_.rfind("n")
            user = str_[loc_start:loc_end - 1]
            if user.find("root") != -1:
                is_root = 1
            else:
                is_root = 0
            is_failure = 1
            is_valid = 1
            return is_failure, is_root, is_valid, user, ip
        elif str_.find("Accepted password for") != -1:
            loc_start = str_.find("Accepted password for ") + len("Accepted password for ")
            loc_end = str_.find(" from")
            user = str_[loc_start:loc_end]
            if user.find("root") != -1:
                is_root = 1
            else:
                is_root = 0
            is_failure = 0
            is_valid = 1
            return is_failure, is_root, is_valid, user, ip
        elif str_.find("Failed password for") != -1:
            loc_start = str_.find("Failed password for ") + len("Failed password for ")
            loc_end = str_.find(" from")
            user = str_[loc_start:loc_end]
            if user.find("root") != -1:
                is_root = 1
            else:
                is_root = 0
            is_failure = 1
            is_valid = 1
            return is_failure, is_root, is_valid, user, ip
        elif str_.find("Invalid user ") != -1:
            loc_start = str_.find("Invalid user ") + len("Invalid user ")
            loc_end = str_.find(" from")
            user = str_[loc_start:loc_end]
            is_root = 0
            is_failure = 1
            is_valid = 0
            return is_failure, is_root, is_valid, user, ip
        else:
            return 0, 0, 0, "-1", ip