# -*- coding:utf-8 -*-

import hashlib

db = {'michael': 'e10adc3949ba59abbe56e057f20f883e', 'bob': '878ef96e86145580c38c87f0410ad153','alice': '99b1c2188db85afee403b1536010c2c9'}
'''
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

md51=hashlib.md5()
md51.update('how to use md5 '.encode('utf-8'))
md51.update('in python hashlib?'.encode('utf-8'))
print(md51.hexdigest())

sha1=hashlib.sha1()
sha1.update('i just wanna get ajob'.encode('utf-8'))
print(sha1.hexdigest())
'''
def login(user,password):
    pas=hashlib.md5()
    pas.update(password.encode('utf-8'))
    if pas.hexdigest()==db[user]:
        return 'ok'
    return None

def main():
    assert login('michael','12345')=='ok','password error'

main()