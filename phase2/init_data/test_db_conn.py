# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   测试数据库链接类
# ------------------------(max to 80 columns)-----------------------------------

from pkg_db.mydb import MyDB

db = MyDB()
tbl_name = 'course_info'

'''
sql = 'SELECT cid,c_name,introduce \
        FROM %s.%s' % (db_name, tbl_name)
'''

sql = 'SELECT cid,c_name,introduce \
        FROM %s' % (tbl_name)

db.cursor.execute(sql)
myresult = db.cursor.fetchall()     # fetchall() 获取所有记录

print(myresult)

for row in myresult:
    print('%s,%s,%s' % (row[0], row[1], row[2]))
