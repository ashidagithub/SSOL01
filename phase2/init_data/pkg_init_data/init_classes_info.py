# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   为班级设置班主任（初始化）
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
tbl_classes = 'classes_info'
tbl_teacher = 'teacher_info'

'''
Step1： 读取所有班级信息，确定有几个班级，
        也就确定了需要找几个班主任
'''
sql = 'SELECT count(*) FROM %s' % tbl_classes
db.cursor.execute(sql)
myresult = db.cursor.fetchall()     # fetchall() 获取所有记录
print(myresult)
teacher_in_charge_num = int(myresult[0][0])
print('We need %d teachers to charge classess.' % teacher_in_charge_num)

'''
Step2：尝试从数据库随机挑选 n 名教师
'''
sql = 'SELECT tid, t_name FROM %s.%s ORDER BY rand() LIMIT %d' % (
    db_name, tbl_teacher, teacher_in_charge_num)
db.cursor.execute(sql)
myresult = db.cursor.fetchall()     # fetchall() 获取所有记录

teacher_list = []
for row in myresult:
    #print('%s' % (row[0]))
    #t = (row[0], row[1])
    t = (row[0])
    teacher_list.append(t)

print('Read database and random fetch teachers into a list...')
print(teacher_list)

'''
Step3：逐一读取班级信息，并将教师分配给班级作为班主任，并更新数据库
'''
sql = 'SELECT class_code FROM %s.%s' % (
    db_name, tbl_classes)

db.cursor.execute(sql)
myresult = db.cursor.fetchall()     # fetchall() 获取所有记录

idx = 0
for c in myresult:
    # 读取班级编号，以及获取教师工号
    class_code = c[0]
    tid = teacher_list[idx]
    idx += 1

    # 更新 班级表中的记录
    sql = 'UPDATE %s.%s ' % (db_name, tbl_classes)
    sql += 'SET '
    sql += 'tid = "%s" ' % tid
    sql += 'WHERE class_code = "%s"' % class_code
    # 执行更新
    db.cursor.execute(sql)

    # [重要] 同步更新教师表中的班级信息
    sql = 'UPDATE %s.%s ' % (db_name, tbl_teacher)
    sql += 'SET '
    sql += 'class_code = "%s" ' % class_code
    sql += 'WHERE tid = "%s"' % tid
    # 执行更新
    db.cursor.execute(sql)

    # 一次性提交两个更新【重要】
    db.commit()
