# -*- coding:utf-8 -*-

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('106.15.179.96',9999))
print(s.recv(1024))
for data in [b'jared',b'colby',b'yin',b'shabi']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
