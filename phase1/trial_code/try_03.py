# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8

# Description:
#   初步学习数据库（单条记录的增删改查）
# ------------------------(max to 80 columns)-----------------------------------

'''
需要安装的第三方库
pip install mysql-connector
'''

import mysql.connector
import random

# Trial 1  数据库的连接
print('\n----- 建立数据库链接... -----')
# 'myconn -> my connection'
myconn = mysql.connector.connect(
    host='localhost',
    database='rmgc20db',
    user='mydev',
    password='liangBa_2019',
    auth_plugin='mysql_native_password',
)

# 'mycursor -> my cursor'
mycursor = myconn.cursor()

# Trial 1 插入一条数据  (增 Insert)
print('\n----- 插入一条数据... -----')
sql = 'INSERT INTO rmgc20db.students (name,sex,birthday) \
       VALUES (%s,%s,%s)'
val = ('Leon',1,'2004/8/16')
mycursor.execute(sql, val)
myconn.commit()

# 利用 for 循环添加 多条 记录
rows = 100
print('\n----- 插入 %d 条数据... -----' % rows )
for idx in range(rows):
    name = 'Leon%03d' % idx
    sex = random.randint(0,1)
    birthday = '2004/8/16'
    val = (name, sex, birthday)
    mycursor.execute(sql, val)
myconn.commit()

# Trial 3 查询数据  (查 Select)
print('\n----- 查询所有数据... -----')
sql = "SELECT * FROM rmgc20db.students LIMIT 300"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
for x in myresult:
  print(x)
