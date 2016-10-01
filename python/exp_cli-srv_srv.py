#!/usr/bin/env python3

import socket
from datetime import datetime, date, time

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

ledValue = {0:'-', 2:'+', 5:'+', 6:'-', 22:'+', 23:'='}

def dataProcessing(inData):
    if inData == '0':
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
        ans = 'You say: ' + inData + '\nbut there is not valid request!\n'
    return u
while 1:
    s.listen(1)
    print('waiting for connection...')
    conn, addr = s.accept()
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: 
            print('Client was disconnected.')
            conn.close()
            break
        else:
            ans = dataProcessing(data)
            print('Client request: ', data)
            print('Server answer: ', ans)
            conn.send(str(ans))
conn.close()

