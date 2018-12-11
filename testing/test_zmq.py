import zmq

context = zmq.Context()

print("Starting Operation...")
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5555")

while True:
    print("Getting Data....")
    x = socket.recv()
    print(x)
