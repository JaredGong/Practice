# -*coding:utf-8 -*-

import requests
'''
r=requests.get(r'https://www.douban.com/')
print(r.status_code)
print(r.text)
'''
r1=requests.get(r'https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(r1.url)
print(r1.encoding)
print(r1.content)

r2=requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r2.json())