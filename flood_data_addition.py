import csv
class FloodDataAddition:
    df = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment', 'urgent',
          'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
          'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 'is_host_login',
          'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
          'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
          'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
          'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
          'dst_host_srv_rerror_rate', 'class']
    def __init__(self):
        print("Initializing data addition modules")
        self.icmp_writer = csv.DictWriter(open('data/ICMP.csv', 'a+'), fieldnames=self.df)
        self.tcp_writer = csv.DictWriter(open('data/TCP.csv', 'a+'), fieldnames=self.df)
        self.udp_writer = csv.DictWriter(open('data/UDP.csv', 'a+'), fieldnames=self.df)
        self.http_writer = csv.DictWriter(open('data/HTTP.csv', 'a+'), fieldnames=self.df)

    def writeICMP(self,df_temp):
        self.icmp_writer.writerow(df_temp)

    def writeTCP(self,df_temp):
        self.tcp_writer.writerow(df_temp)

    def writeUDP(self,df_temp):
        self.udp_writer.writerow(df_temp)

    def writeHTTP(self,df_temp):
        self.http_writer.writerow(df_temp)
