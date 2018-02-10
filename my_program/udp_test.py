# -*- coding:utf-8 -*-

import socket,time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'jared',b'unkonw',b'unkonw',b'unkonw',b'unkonw',b'unkonw']:
    s.sendto(data,('106.15.179.96',9999))
    print(s.recv(1024).decode('utf-8'))
    time.sleep(5)
s.close()