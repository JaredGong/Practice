# -*- coding:utf-8 -*-

import base64

def safe_base64_decode(b):
    remainder=len(b)%4
    if remainder==0:
        s=base64.b64decode(b)
    elif remainder==2:
        s=base64.b64decode(b+b'==')
    else:
        s=base64,b64decode(b+b'=')
    return s

def main():
    b=b'YWJjZA'
    b=safe_base64_decode(b)
    print(b)

main()
'''
be=base64.b64encode(b'binary\x00string')
print(be)
bd=base64.b64decode(be)
print(bd)

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
'''