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

# Step 1  数据库的连接
myconn = mysql.connector.connect(
    host='211.167.105.132',
    database='stdt201909',
    user='student001',
    password='liangBa_2019',
    auth_plugin='mysql_native_password',
)
print(myconn)

# Step 2  创建一张表
mycursor = myconn.cursor()
sql = 'CREATE TABLE IF NOT EXISTS stdt001( \
    id INT UNSIGNED AUTO_INCREMENT, \
    name VARCHAR(10), \
    class INTEGER, \
    PRIMARY KEY(id) \
)'
mycursor.execute(sql)

# Step 3 插入一条数据  (增 Insert)
sql = "INSERT INTO stdt001 (name, class) VALUES (%s, %s)"
val = ("张三", 2)
mycursor.execute(sql, val)
myconn.commit()

# Step 4 查询一条数据  (查 Select)
sql = "SELECT * FROM stdt001"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
print('\n----- 查询所有 -----')
for x in myresult:
  print(x)

print('\n----- 查询指定条件 -----')
sql = "SELECT * FROM stdt001 WHERE name=%s AND class=%s"
val = ("张三", 2)
mycursor.execute(sql, val)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
for x in myresult:
  print(x)

# Step5 删除一条数据 (删 Delete)
print('\n----- 开始删除... -----')
sql = "DELETE FROM stdt001 WHERE name=%s AND class=%s"
val = ("张三", 2)
mycursor.execute(sql, val)
myconn.commit()

print('\n----- 删除完毕后再查询 -----')
sql = "SELECT * FROM stdt001"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
print('\n----- 查询所有 -----')
for x in myresult:
  print(x)
