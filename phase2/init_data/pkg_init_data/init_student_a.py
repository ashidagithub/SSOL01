# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   添加 n个学生（初始化）
# ------------------------(max to 80 columns)-----------------------------------

import random
import sys
# ---------------------------------------------------
sys.path.append('..')
# ---------------------------------------------------
from pkg_generators.naming_machine import pick_a_full_name_by_sex as pfnbs
from pkg_generators.naming_machine import pick_a_full_name as pfn
from pkg_generators.birthday_generator import generate_birthday as gbd
from pkg_db.mydb import MyDB


def allocate_to_class(birthday):

    # 依据生日确定年级
    # 2000.9-2001.8 高三
    # 2001.9-2002.8 高二
    # 2002.9-2003.8 高一
    if birthday.year == 2000:
        class_grade = 3
    elif birthday.year == 2001:
        if birthday.month <= 8:
            class_grade = 3
        else:
            class_grade = 2
    elif birthday.year == 2002:
        if birthday.month <= 8:
            class_grade = 2
        else:
            class_grade = 1
    else:
        class_grade = 1

    # 依据年级随机分配班级，并返回班级编号
    db = MyDB()
    db_name = 'rmgc20_student'
    tbl_classes = 'classes_info'

    sql = 'SELECT class_code '
    sql += 'FROM %s.%s ' % (db_name, tbl_classes)
    sql += 'WHERE class_grade = %s ' % class_grade
    sql += 'ORDER BY rand() LIMIT 1'
    db.cursor.execute(sql)
    myresult = db.cursor.fetchall()     # fetchall() 获取所有记录

    class_code = myresult[0][0]

    return class_code


# 涉及到本模块操作的所有数据库和表名称
db = MyDB()
db_name = 'rmgc20_student'
tbl_students = 'student_info'
tbl_classes = 'classes_info'

# 先清空学生表
sql = 'DELETE FROM %s.%s' % (db_name, tbl_students)
db.cursor.execute(sql)
db.commit()

'''
Step1：先读取所有班级
Step2：随机产生一批学生
Step3：根据学生的生日，分配至合适的年级；随机指定班级
'''
sql = 'SELECT class_code '
sql += 'FROM %s.%s ' % (db_name, tbl_classes)
db.cursor.execute(sql)
myresult = db.cursor.fetchall()     # fetchall() 获取所有记录
print(myresult)

num = 1000
for idx in range(num):
    sex = random.randint(1, 2)
    student_name = pfnbs(sex)
    birthday = gbd(False)
    class_code = allocate_to_class(birthday)
    #print(s_birthday, class_code)

    sql = 'INSERT INTO %s.%s ' % (db_name, tbl_students)
    sql += '(class_code,student_name,s_sex,s_birthday,comments) '
    sql += 'VALUES ('
    sql += '"%s","%s",%d,"%s","%s"' % (
        class_code, student_name, sex, birthday, '备注内容xxxx')
    sql += ')'
    db.cursor.execute(sql)
db.commit()

'''
INSERT INTO rmgc20_student.student_info
(sid,class_code,student_name,s_sex,s_birthday,comments)
VALUES
(<{sid: }>,
<{class_code: }>,
<{student_name: }>,
<{s_sex: }>,
<{s_birthday: }>,
<{comments: }>);
'''
