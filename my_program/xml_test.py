# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name,str(attrs)))

    def end_element(self,name):
        print('sax:end_element: %s' % name)

    def char_data(self,text):
        print('sax:char_data: %s'% text)

URL='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL) as f:
    xml=f.read().decode('utf-8')

handler=DefaultSaxHandler()
parse=ParserCreate()
parse.StartElementHandler=handler.start_element
parse.EndElementHandler=handler.end_element
parse.CharacterDataHandler=handler.char_data
parse.Parse(xml)
