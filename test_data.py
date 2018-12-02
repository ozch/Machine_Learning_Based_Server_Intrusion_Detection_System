from data_process import DataProcess
from  flood_predict import FloodPerdiction

fp = open('test_data.txt') # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines

import zmq

context = zmq.Context()

print("Connecting to hello world server…")
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:5555")

for line in lines:
    socket.send_string(line)

fp.close() # Close file