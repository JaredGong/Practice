# -*- coding:utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

smtp_server='smtp.qq.com'
smtp_port=587
from_addr='448218127@qq.com'
password='tvvgjznyowrwbjed'
to_addr='448218127@qq.com'
#msg=MIMEText('hello, send by my python...','plain','utf-8')
#msg=MIMEText('<html><body><h1>Hello</h1>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>'+'</body></html>','html','utf-8')
msg=MIMEMultipart('alternative')
#msg['From']=_format_addr('python 爱好者 <%s>' % from_addr)
msg['From']=Header('python 爱好者呀','utf-8').encode()
msg['To']=_format_addr('管理员 <%s>' % to_addr)
msg['Subject']=Header('来自SMTP的问候....','utf-8').encode()
msg.attach(MIMEText('<html><body><h1>Hello</h1>'+'<p><img src="cid:0"></p>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>'+'</body></html>','html','utf-8'))
msg.attach(MIMEText('hello, send by my python...','plain','utf-8'))
with open(r'C:\Users\44821\Desktop\code.jpg','rb') as f:
    mime=MIMEBase('image','jpg',filename='test.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


server=smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()