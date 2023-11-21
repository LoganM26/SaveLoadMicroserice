import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Send a single request containing the save code "011111001", 
#  with a file path of "C:\Users\logan\OneDrive\Documents\CS361\Microservice\\tester.txt"

print(f"Sending request")
socket.send(b"011111001,C:\Users\logan\OneDrive\Documents\CS361\Microservice\\tester.txt")

#  Get the reply.
message = socket.recv()
print(f"Received reply [ {message} ]")
