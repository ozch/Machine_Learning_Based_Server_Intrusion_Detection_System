import pickle
from  flood_predict import FloodPerdiction



fp = FloodPerdiction()
print(type(http_model))
result=fp.predictUDPTCP(http_model,[0,5,232,8153,0,0])
print(type(http_model))
print(type(result))
#import zmq
#import time

#context = zmq.Context()
# Socket to talk to server
#print("Creating socket and connecting to extractor ...")
#socket = context.socket(zmq.REP)
#socket.bind("tcp://*:5555")

# Do 10 requests, waiting each time for a response
#while True:
#    message = socket.recv()
#    print("Received request: %s" % message)
#    socket.send(b"World")