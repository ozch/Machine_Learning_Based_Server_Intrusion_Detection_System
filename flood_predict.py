import sklearn
from sklearn.ensemble import RandomForestRegressor
import joblib
import pickle
import warnings
from flood_data_process import DataProcess
from flood_data_addition import FloodDataAddition
warnings.simplefilter(action='ignore', category=FutureWarning)
class FloodPerdiction:
    http_model = RandomForestRegressor()
    def __init__(self):
        #TODO check if model exist other wise create a model first by calling nsl_kdd_*.py files and using the model.
        # loading all three flooding models
        self.dp = DataProcess()
        self.fda= FloodDataAddition()
        print("Loading Models:")
        http_fname = "models/http_svc.pkl"
        print("Loading " + http_fname + "...")
        self.http_model = pickle.load(open(http_fname, 'rb'))

        icmp_fname = "models/icmp_rfr.pkl"
        print("Loading " + icmp_fname + "...")
        self.icmp_model = pickle.load(open(icmp_fname, 'rb'))

        udp_fname = "models/udp_rfr.pkl"
        print("Loading " + udp_fname + "...")
        self.udp_model = pickle.load(open(udp_fname, 'rb'))

        tcp_fname = "models/tcp_svc.pkl"
        print("Loading " + tcp_fname + "...")
        self.tcp_model = pickle.load(open(tcp_fname, 'rb'))

    def predictHTTP(self,dict):
        perdict = self.http_model.predict([self.dp.prepareList(dict)])
        per = perdict[0]
        str_ = ""
        if per <= 0.6:
            str_ = 'normal'
        else:
            str_ = 'anomaly'
        dict_temp = dict.copy()
        dict_temp.update({'class':str_})
        dict_temp.update({'service': 'http'})
        dict_temp.update({'protocol_type': 'tcp'})
        self.fda.writeHTTP(dict_temp)
        return per
    #Todo refector the code which labels anomaly and normal, or just leave it there who's gonna notice
    def predictUDP(self,dict):
        perdict = self.udp_model.predict([self.dp.prepareList(dict)])
        per = perdict[0]
        str_ = ""
        if per <= 0.6:
            str_ = 'normal'
        else:
            str_ = 'anomaly'
        dict_temp = dict.copy()
        dict_temp.update({'class': str_})
        dict_temp.update({'protocol_type': 'udp'})
        self.fda.writeUDP(dict_temp)
        return per

    def predictTCP(self,dict):
        perdict = self.tcp_model.predict([self.dp.prepareList(dict)])
        per = perdict[0]
        str_ = ""
        if per <= 0.6:
            str_ = 'normal'
        else:
            str_ = 'anomaly'
        dict_temp = dict.copy()
        dict_temp.update({'class': str_})
        dict_temp.update({'protocol_type': 'tcp'})
        self.fda.writeTCP(dict_temp)
        return per

    def predictICMP(self,dict):
        perdict = self.icmp_model.predict([self.dp.prepareList(dict)])
        per = perdict[0]
        str_ = ""
        if per <= 0.6:
            str_ = 'normal'
        else:
            str_ = 'smurf'
        dict_temp = dict.copy()
        dict_temp.update({'class': str_})
        dict_temp.update({'protocol_type': 'icmp'})
        self.fda.writeICMP(dict_temp)
        return per

    def perdictAnomaly(self,protocol,dict):
        if(protocol == 1):
            x = self.predictICMP(dict)
        elif(protocol == 2):
            x = self.predictHTTP(dict)
        elif (protocol == 3):
            x = self.predictUDP(dict)
        elif (protocol == 4):
            x = self.predictTCP(dict)
        else:
            print("To Something")
        return x
