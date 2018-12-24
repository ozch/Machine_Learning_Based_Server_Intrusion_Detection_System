
import zmq
from flood_data_process import DataProcess
from  flood_predict import FloodPerdiction
import traceback
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
        msg = str(message)
        print("RECEIVED INSTANCE : " + str(msg))
        print(len(msg))
        if(len(msg)<50):
            continue
        try:
            protocol, instance = dp.prepareInstance(str(msg))
            #print(str(protocol) + ">" + str(instance))
            result = fp.perdictAnomaly(protocol, instance)
        except:
            traceback._cause_message
            traceback._context_message
            traceback.print_exc()
            result = "Exception: An Error Occurred While Predicting Value"
        print("Attack : " +str(result))
        print("_______________________________________________________")
    except:
        traceback._cause_message
        traceback._context_message
        traceback.print_exc()
        print("Exception : An Error Occurred, ZeroMQ")
