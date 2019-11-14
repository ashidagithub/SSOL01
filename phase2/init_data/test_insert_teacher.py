# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   测试插入教师的数据
# ------------------------(max to 80 columns)-----------------------------------

import random

from pkg_db.mydb import MyDB
from pkg_generators.birthday_generator import generate_birthday as gbd
from pkg_generators.work_number_generator import generate_worker_number as gwn
from pkg_generators.naming_machine import pick_a_full_name as pfn
from pkg_generators.naming_machine import pick_a_full_name_by_sex as pfnbs

# try to insert 1 row
tbl_name = 'teacher_info'

is_teacher = True
is_man = 1

tid = gwn()
class_code = ''
name = pfnbs(is_man)
sex = is_man
birthday = gbd(is_teacher)
in_charge = True

sql = 'INSERT INTO %s ' % tbl_name
sql += '(tid,class_code,t_name,t_sex,t_birthday,in_charge) '
sql += 'VALUES ('
sql += '"%s","%s","%s",%d,"%s",%s' % (
    tid, class_code, name, sex, birthday, in_charge)
sql += ')'

print(sql)
db = MyDB()
db.cursor.execute(sql)
db.commit()


# try to insert many
tbl_name = 'teacher_info'
is_teacher = True
db = MyDB()

for idx in range(1000):
    is_man = random.randint(1, 2)

    tid = gwn()
    class_code = ''
    name = pfnbs(is_man)
    sex = is_man
    birthday = gbd(is_teacher)
    in_charge = False

    sql = 'INSERT INTO %s ' % tbl_name
    sql += '(tid,class_code,t_name,t_sex,t_birthday,in_charge) '
    sql += 'VALUES ('
    sql += '"%s","%s","%s",%d,"%s",%s' % (
        tid, class_code, name, sex, birthday, in_charge)
    sql += ')'

    # print(sql)
    db.cursor.execute(sql)

db.commit()
