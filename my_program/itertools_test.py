# -*- coding:utf-8 -*-

import itertools
'''
natuals=itertools.count(1)
for n in natuals:
    print(n)

cy=itertools.cycle('abc')
n=0
for c in cy:
    print(c)
    n+=1
    if n==10:
        break

na=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,na)
print(list(ns))
'''
def pi(n):
    s=0
    p=itertools.count(1,2)
    for i in range(1,n):
        if i%2==1:
            s=s+4/next(p)
        else:
            s=s-4/next(p)
    return s

for n in [10,100,1000,10000]:
    print(pi(n))