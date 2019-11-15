# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   建立课程与教师之间的关系（初始化）
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
tbl_teacher = 'teacher_info'
tbl_t_c = 'teacher_course'

'''
Step1：将所有课程信息读取到列表中去
'''
sql = 'SELECT cid FROM %s.%s' % (db_name, tbl_course)
db.cursor.execute(sql)
myresult = db.cursor.fetchall()     # fetchall() 获取所有记录

course_list = []
for row in myresult:
    print('%s' % (row[0]))
    course_list.append(row[0])

print('Read database and fetch data into a list...')
print(course_list)

'''
Step2: 清除所有已有的 “教师-课程”关系表
'''
sql = 'DELETE FROM %s.%s' % (db_name, tbl_t_c)
db.cursor.execute(sql)
db.commit()

'''
Step3：顺序读取所有教师的信息，随机选取一个课程后插入到 “教师-课程”关系表
'''
sql = 'SELECT tid FROM %s.%s' % (db_name, tbl_teacher)
db.cursor.execute(sql)
myresult = db.cursor.fetchall()     # fetchall() 获取所有记录

for row in myresult:
    tid = row[0]
    cid = random.choice(course_list)

    sql = 'INSERT INTO %s.%s ' % (db_name, tbl_t_c)
    sql += '(tid,cid) '
    sql += 'VALUES ('
    sql += '"%s","%s"' % (tid, cid)
    sql += ')'
    db.cursor.execute(sql)

db.commit()

'''
Step4：查看每门课程的授课老师清单
'''
for c in course_list:
    sql = 'SELECT %s.c_name, ' % tbl_course
    sql += '%s.tid, ' % tbl_t_c
    sql += '%s.t_name ' % tbl_teacher
    sql += 'FROM %s, %s, %s ' % (tbl_course, tbl_t_c, tbl_teacher)
    sql += 'WHERE %s.cid="%s" ' % (tbl_course, c)
    sql += 'AND %s.cid = %s.cid ' % (tbl_course, tbl_t_c)
    sql += 'AND %s.tid = %s.tid ' % (tbl_t_c, tbl_teacher)
    db.cursor.execute(sql)
    myresult = db.cursor.fetchall()     # fetchall() 获取所有记录
    print('Course [%s]----------' % c )
    for row in myresult:
        print('%s,%s,%s' % (row[0],row[1],row[2]))

'''
SELECT course_info.c_name,
       teacher_course.tid,
       teacher_info.t_name
FROM course_info,
     teacher_course,
     teacher_info
WHERE course_info.cid = "GZSX0201"
  AND course_info.cid = teacher_course.cid
  AND teacher_course.tid = teacher_info.tid
'''
