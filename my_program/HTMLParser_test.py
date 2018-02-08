# -*- coding:utf-8 -*-

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)

    def handle_endtag(self, tag):
        print(tag)

    def handle_startendtag(self, tag, attrs):
        print(tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print(data)

    def handle_entityref(self, name):
        print(name)

    def handle_charref(self, name):
        print(name)

data='''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>'''
parser=MyHTMLParser()
parser.feed(data)