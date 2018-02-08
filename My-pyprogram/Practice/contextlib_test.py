# -*- condig:utf-8 -*-

import contextlib,urllib.request
'''
class Query(object):

    def __init__(self,name):
        self.name=name

    def __enter__(self):
        print('begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('error')
        else:
            print('end')

    def query(self):
        print(self.name)

with Query('jared') as q:
    q.query()
'''
'''
class Query(object):

    def __init__(self,name):
        self.name=name

    def query(self):
        print(self.name)

@contextlib.contextmanager
def create_query(name):
    print('begin')
    q=Query(name)
    yield q
    print('end')

with create_query('jared') as q:
    q.query()
'''

with contextlib.closing(urllib.request.urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

'''
class Query(object):

    def __init__(self,name):
        self.name=name

    def query(self):
        return self.name


with contextlib.closing(Query('jared').query()) as q:
    for i in q:
        print(i)
'''