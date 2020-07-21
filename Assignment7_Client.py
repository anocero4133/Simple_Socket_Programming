#!/usr/bin/python

import socket, pickle, sys
from Assignment7_Data import Assign7Data

a = Assign7Data(88,27).AddVars()

HOST = '127.0.0.1'
PORT = 40005
PORT2 = 40006
Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock.connect((HOST,PORT))

dataVar = a
sendData = pickle.dumps(dataVar)
Sock.send(sendData)
Sock.close()
print("Data sent")

Sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock2.bind((HOST, PORT2))
Sock2.listen(1)
conn, addr = Sock2.accept()

recvdata = conn.recv(4096)
result = pickle.loads(recvdata)
conn.close()
print("this is the result: ",result)
sys.stdout.write(str(result))
