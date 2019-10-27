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

# Trial 1  数据库的连接
print('\n----- 建立数据库链接... -----')
myconn = mysql.connector.connect(
    host='localhost',
    database='rmgc20db',
    user='mydev',
    password='liangBa_2019',
    auth_plugin='mysql_native_password',
)
#print(myconn)
mycursor = myconn.cursor()

# Trial 2  创建一张表
print('\n----- 新建一张表... -----')
sql = 'CREATE TABLE IF NOT EXISTS students( \
    id INT UNSIGNED AUTO_INCREMENT, \
    name VARCHAR(10), \
    class INTEGER, \
    PRIMARY KEY(id) \
)'
mycursor.execute(sql)

# Trial 3 插入一条数据  (增 Insert)
print('\n----- 插入一条数据... -----')
sql = "INSERT INTO students (name, class) VALUES (%s, %s)"
val = ("张三", 2)
mycursor.execute(sql, val)
myconn.commit()

# Trial 4 查询一条数据  (查 Select)
print('\n----- 查询所有数据... -----')
sql = "SELECT * FROM students"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
for x in myresult:
  print(x)

print('\n----- 查询指定条件的 -----')
sql = "SELECT * FROM students WHERE name=%s AND class=%s"
val = ("张三", 2)
mycursor.execute(sql, val)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
for x in myresult:
  print(x)

# Trial5 更改某条符合条件的记录
print('\n----- 更改数据 -----')
sql = "UPDATE students SET name = '张三改' WHERE name = '张三'"
mycursor.execute(sql)
myconn.commit()

print('\n----- 更改完毕后再查询 -----')
sql = "SELECT * FROM students"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
print('\n----- 查询所有 -----')
for x in myresult:
    print(x)

# Trial6 删除一条数据 (删 Delete)
print('\n----- 开始删除... -----')
sql = "DELETE FROM students WHERE name=%s AND class=%s"
val = ("张三", 2)
mycursor.execute(sql, val)
myconn.commit()

print('\n----- 删除完毕后再查询 -----')
sql = "SELECT * FROM students"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
print('\n----- 查询所有 -----')
for x in myresult:
  print(x)

# Trial7 删除整张表 ( Drop )
print('\n----- 开始删除表... -----')
sql = "DROP TABLE students"
mycursor.execute(sql)
myconn.commit()

# Trial8 关闭数据库链接
print('\n----- 关闭数据库链接... -----')
myconn.close()
