# -*- coding:utf-8 -*-

import mysql.connector

conn=mysql.connector.connect(host='106.15.179.96',port='3306',user='root',password='q111111',database='test')
cursor=conn.cursor()
#cursor.execute('create table data (id int(10) primary key, str varchar(20))')
#cursor.execute('insert into data(id,str) values (%s,%s)', ['1','jared'])
#print(cursor.rowcount)
#conn.commit()
#cursor.close()
#cursor=conn.cursor()
cursor.execute('select * from data')
print(cursor.fetchall())
cursor.close()
conn.close()