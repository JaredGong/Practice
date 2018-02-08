# -*- coding:utf-8 -*-

'a test py'

from datetime import datetime,timedelta,timezone

def to_timestamp(time,zone):
    utctime=datetime.strptime(time,'%Y-%m-%d %H:%M:%S')


'''
now=datetime.now()
print(now)
print(type(now))
'''
'''
dt=datetime(2018,2,2,16,10,0)
print(dt.timestamp())
'''
'''
tday=datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(tday)
'''
'''
now=datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

print(now + timedelta(hours=10))
'''
def main():
    time,zone=map(input(),('please input time(like2015-1-21 9:01:30):  ','please input timezong(like UTC+5:00):'))


main()

