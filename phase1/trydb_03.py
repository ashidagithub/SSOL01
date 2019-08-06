# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8

# Description:
#   初步学习数据库（更改单条或多条记录）
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
mycursor = myconn.cursor()

# Step2 清空及添加记录
print('\n----- 开始删除... -----')
sql = "DELETE FROM stdt001"
mycursor.execute(sql)

print('\n----- 批量添加数据 -----')
myconn.commit()
sql = "INSERT INTO stdt001 (name, class) VALUES (%s, %s)"
val = [
    ("张三", 1),
    ("李四", 2),
    ("王五", 3),
]
mycursor.executemany(sql, val)
myconn.commit()

print('\n----- 添加完毕后再查询 -----')
sql = "SELECT * FROM stdt001"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
print('\n----- 查询所有 -----')
for x in myresult:
    print(x)

# Step3 更改某条符合条件的记录
print('\n----- 开始更改数据 -----')
sql = "UPDATE stdt001 SET name = '张三改' WHERE name = '张三'"
mycursor.execute(sql)
myconn.commit()

print('\n----- 更改完毕后再查询 -----')
sql = "SELECT * FROM stdt001"
mycursor.execute(sql)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
print('\n----- 查询所有 -----')
for x in myresult:
    print(x)
