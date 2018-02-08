# -*- coding:utf-8 -*-

import hashlib,random,hmac

db={}

def get_hamc(key,password):
    return hmac.new(key.encode('utf-8'),password.encode('utf-8'),'MD5').hexdigest()

class User(object):
    def __init__(self,username,password):
        self.username=username
        self.password=get_hamc(self.username,password)
        db[self.username]=self.password

def login(username,password):
    if get_hamc(username,password)==db[username]:
        print('ok')
    else:
        print('password error')

def main():
    while True:
        m=input('please enter \'login\' or \'register\' or \'out\'to choose execution: ')
        if m=='login':
            u=input('please enter your username: ')
            p=input('please enter your password: ')
            login(u, p)
        elif m=='register':
            u=input('please enter your username: ')
            p=input('please enter your password: ')
            User(u,p)
        elif m=='out':
            break
        else:
            print('you input is invalid')
    print('end')

main()