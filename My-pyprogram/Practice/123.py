# -*- coding:utf-8 -*-
import hashlib,base64

sha=hashlib.sha256()
#sha.update(base64.b64encode(b'16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48'))
#print(base64.b64encode(bytes.fromhex(sha.hexdigest())))
sha.update(b'16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48')
print(base64.b64decode(sha.hexdigest()))