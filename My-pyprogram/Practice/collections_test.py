# -*- coding:utf-8 -*-

from collections import namedtuple,deque,defaultdict,OrderedDict
'''
point=namedtuple('point',['x','y'])
p=point(2,3)
print(p.x,p.y)

q=deque(['a','b','c'])
print(q)
q.append('r')
q.appendleft('l')
print(q)

d=defaultdict(lambda :'fan de si')
d[1]=123
print(d[1],d[2])

dd=OrderedDict([(1,1),(3,2),(2,1)])
print(dd)
'''
class LastUpadateOrederedDict(OrderedDict):

    def __init__(self,capacity):
        super(LastUpadateOrederedDict, self).__init__()
        self._capacity=capacity

    def __setitem__(self, key, value):
        containskey=1 if key in self else 0
        if len(self) - containskey >=self._capacity:
            last=self.popitem(last=False)
            print('remove',last)
        if containskey:
            del self[key]
            print('set',(key,value))
        else:
            print('add',(key,value))
        OrderedDict.__setitem__(self,key,value)

def main():
    d=LastUpadateOrederedDict(6)
    for i in range(10):
        d.__setitem__(i,1)
        print(d)

main()