import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def saveFunction(msg, fileName) -> None:
        
    print(fileName + "save")
    with open(fileName, "w") as txt_file:
        
        txt_file.write(msg)
        txt_file.close()
        

def loadFunction(fileName) -> str:

    print(fileName + "load")
    with open(fileName, "R") as txt_file:

        msg = txt_file.read()
        txt_file.close()

    return msg

while True:

    saveComp, loadComp = False, False

    #  Wait for next request from client
    message = socket.recv()
    print(f"Received request: {message}")
    message = message.decode()
    message = message.split(',')
      
    #  Do some 'work'\
    if(message[0][0] == "0"):
        
        saveFunction(message[0][1:], message[1])
        saveComp = True

    elif(message[0][0] == '1'):

        msg = loadFunction(message[1])
        msg = msg.encode()
        loadComp = True
        
    #  Send reply back to client
    if(saveComp):
        
        socket.send(b"Save Successful.")
        print(message[1])

    elif(loadComp):

        socket.send(bytes(msg, encoding="UTF-8"))
        print(message[1])
        print(msg)
