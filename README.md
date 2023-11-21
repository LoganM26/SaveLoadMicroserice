# SaveLoadMicroserice

The user must first create a connection to the ZeroMQ server. This is done by
importing zmq, which is then used initially in setting up a server connection,
or socket. First, the user must configure the socket using zmq.Context(zmq.REQ).
Then, they are able to access a port using the .connect() method. Now, the user
is able to send and recieve messages, provided the server side is operational.
The user can use socket.send() in order to send messages across the connection.
This message is then parsed and worked on by the microservice. Now, all the user
has to do is call socket.recv(), and wait for the server to respond with the 
expected result.

Example Request:

![image](https://github.com/LoganM26/SaveLoadMicroserice/assets/148154868/ecf6f5d8-b09d-4de4-88bf-15352f43cab3)


Example Console Return:

![image](https://github.com/LoganM26/SaveLoadMicroserice/assets/148154868/1758588d-9919-4133-9e1d-6fcd2b762056)


Example Text Output:

![image](https://github.com/LoganM26/SaveLoadMicroserice/assets/148154868/97fe441a-4730-49d4-b352-1cde072db37e)
