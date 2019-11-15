# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   建立学生选课关系表（初始化）
# ------------------------(max to 80 columns)-----------------------------------

import random
import sys
# ---------------------------------------------------
sys.path.append('..')
# ---------------------------------------------------
from pkg_db.mydb import MyDB

# 涉及到本模块操作的所有数据库和表名称
db = MyDB()
db_name = 'rmgc20_student'
tbl_course = 'course_info'
tbl_student = 'student_info'
tbl_s_c = 'student_course'

'''
Step1：将所有课程信息读取到列表中去
'''
sql = 'SELECT cid FROM %s.%s' % (db_name, tbl_course)
db.cursor.execute(sql)
myresult = db.cursor.fetchall()     # fetchall() 获取所有记录

course_list = []
for row in myresult:
    #print('%s' % (row[0]))
    course_list.append(row[0])

print('Read database and fetch data into a list...')
print(course_list)

'''
Step2: 清除所有已有的 “学生-课程”关系表
'''
sql = 'DELETE FROM %s.%s' % (db_name, tbl_s_c)
db.cursor.execute(sql)
db.commit()

'''
Step3：顺序读取所有学生的信息，随机选取1-5个课程后插入到 “学生-课程”关系表
需要对 “课程” 表重新设计，添加学生年级与课程的对应关系！

'''
