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
        http_fname = "models/http_rfr.pkl"
        print("Loading " + http_fname + "...")
        self.http_model = pickle.load(open(http_fname, 'rb'))

        icmp_fname = "models/icmp_rfr.pkl"
        print("Loading " + icmp_fname + "...")
        self.icmp_model = pickle.load(open(icmp_fname, 'rb'))

        udp_tcp_fname = "models/udp_tcp_rfr.pkl"
        print("Loading " + udp_tcp_fname + "...")
        self.udp_tcp_model = pickle.load(open(udp_tcp_fname, 'rb'))
    def predictHTTP(self,instance):
        perdict = self.http_model.predict([instance])
        return perdict[0]
    def predictUDPTCP(self,instance):
        perdict = self.udp_tcp_model.predict([instance])
        return perdict[0]
    def predictICMP(self,instance):
        perdict = self.icmp_model.predict([instance])
        return perdict[0]
    def perdictAnomaly(self,protocl,instance):
        if(protocl == 1):
            x = self.predictICMP(instance)
        elif(protocl == 2):
            x = self.predictHTTP(instance)
        else:
            x = self.predictUDPTCP(instance)
        return x
