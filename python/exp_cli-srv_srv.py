#!/usr/bin/env python

import socket
from datetime import datetime, date, time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

ledValue = {0:'-', 2:'+', 5:'+', 6:'-', 22:'+', 23:'='}

print 'waiting for connection...'

conn, addr = s.accept()

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: 
        print 'Client was disconnected.'
        break
    if data == '0\n':
        timeNow = datetime.now()
        try:
            if ledValue[timeNow.hour] == '+':
                ans = round( ( timeNow.minute / 60.0 ) * 255 )
            elif ledValue[timeNow.hour] == '=':
                ans = 255
            elif ledValue[timeNow.hour] == '-':
                ans = round( ( 255 - ( timeNow.minute / 60.0 ) * 255 ) )
        except KeyError:
            ans = 0
    else:
        ans = 'You say: ' + data + 'but there is not valid request!\n'
    print 'Client request: ', data
    print 'Server answer: ', ans
    conn.send(str(ans))
conn.close()

