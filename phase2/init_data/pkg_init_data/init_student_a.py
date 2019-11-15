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
from pkg_db.mydb import MyDB
from pkg_generators.birthday_generator import generate_birthday as gbd
from pkg_generators.naming_machine import pick_a_full_name as pfn
from pkg_generators.naming_machine import pick_a_full_name_by_sex as pfnbs

# 涉及到本模块操作的所有数据库和表名称
db = MyDB()
db_name = 'rmgc20_student'
tbl_students = 'student_info'

# 先清空学生表
sql = 'DELETE FROM %s.%s' % (db_name, tbl_students)


# 生成高一年级学生
num = 300
for idx in range(num):


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
