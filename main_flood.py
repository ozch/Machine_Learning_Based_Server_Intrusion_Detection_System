
import zmq
from data_process import DataProcess
from  flood_predict import FloodPerdiction
#TODO Implement self learning by saving data into database or file and learning from it

context = zmq.Context()
# Socket to talk to server
print("Starting Operation...")
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5555")

fp = FloodPerdiction()
dp = DataProcess()
while True:
    try:
        message = socket.recv_string()
        print("REC: " + message)
        if(len(message)<50):
            continue
        try:
            protocol, instance = dp.prepareInstance(message)
            print(str(protocol) + ">" + str(instance))
            result = fp.perdictAnomaly(protocol, instance)
        except:
            result = "-1"
        print(result)
    except:
        print("ERROR!!!")
