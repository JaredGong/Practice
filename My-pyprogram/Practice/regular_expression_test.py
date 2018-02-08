# -*- conding:utf-8 -*-

'a test py'

import re

re_email=re.compile(r'^([a-zA-Z0-9.]{1,20})@([a-zA-Z0-9.]{1,20})$')

def is_valid_email(addr):
    if re_email.match(addr):
        email=re_email.match(addr)
        print('the email name is \"%s\",postfix is \"%s\"' %(email.group(1),email.group(2)))
    else:
        print('the emailaddress is invalid')

'''
a=re.split(r'[\s\,\;]+','a,;;b,c  ff  ,d')
print(a)
'''
'''
t='19:06:45'
m=re.match(r'^([0-9]|0[0-9]|1[0-9]|2[0-9])\:([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|)\:([0-9]|0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])$',t)
print(m.groups())
'''
email=input('please enter a email address:')
is_valid_email(email)
