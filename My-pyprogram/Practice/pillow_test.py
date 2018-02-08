# -*- coding:utf-8 -*-

from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

def rndchar():
    return chr(random.randint(65,90))

def rndcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndcolor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))

font=ImageFont.truetype(r'D:\python3\pycharm\PyCharm Community Edition 2017.3.3\jre64\lib\fonts\DroidSerif-Bold.ttf',36)

draw=ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndcolor())

for t in range(4):
    draw.text((60*t+10,10),rndchar(),font=font,fill=rndcolor2())

image=image.filter(ImageFilter.BLUR)
image.save(r'C:\Users\44821\Desktop\code.jpg')