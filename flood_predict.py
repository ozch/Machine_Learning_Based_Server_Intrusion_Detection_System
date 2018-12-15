import sklearn
from sklearn.ensemble import RandomForestRegressor
import joblib
import pickle
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
class FloodPerdiction:
    http_model = RandomForestRegressor()
    def __init__(self):
        #TODO check if model exist other wise create a model first by calling nsl_kdd_*.py files and using the model.
        # loading all three flooding models
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

    def predictHTTP(self,instance):
        perdict = self.http_model.predict([instance])
        return perdict[0]
    def predictUDP(self,instance):
        perdict = self.udp_model.predict([instance])
        return perdict[0]
    def predictTCP(self,instance):
        perdict = self.tcp_model.predict([instance])
        return perdict[0]
    def predictICMP(self,instance):
        perdict = self.icmp_model.predict([instance])
        return perdict[0]
    def perdictAnomaly(self,protocol,instance):
        if(protocol == 1):
            x = self.predictICMP(instance)
        elif(protocol == 2):
            x = self.predictHTTP(instance)
        elif (protocol == 3):
            x = self.predictUDP(instance)
        else:
            x = self.predictTCP(instance)
        return x
