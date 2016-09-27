#!/usr/bin/env python

import socket
from sys import stdin

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while 1:
    MESSAGE = stdin.readline()
    if MESSAGE == 'exit\n' or MESSAGE == '\n':
        break
    #print MESSAGE
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    print "recived data:", data

s.close()

