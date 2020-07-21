#!/usr/bin/python

import socket
import pickle
import sys

HOST = '127.0.0.1'
PORT = 40005
PORT2 = 40006
Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock.bind((HOST,PORT))
Sock.listen(1)
connector, addr = Sock.accept()

data = connector.recv(4096)
result = pickle.loads(data)
print('Data recieved')

connector.close()
print(result)


Sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Sock2.connect((HOST,PORT2))
sendData = pickle.dumps(result)
Sock2.send(sendData)
Sock2.close()
print("Sent BACK")
