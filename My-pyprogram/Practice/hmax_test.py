# -*- coding:utf-8 -*-

import hmac

messaage=b'Hello, world!'
key=b'secret'
p=hmac.new(key,messaage,digestmod='MD5')
print(p.hexdigest())