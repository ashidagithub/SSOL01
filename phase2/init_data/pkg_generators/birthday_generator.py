# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.10

# Description:
#   创建一个产生教师或学生生日的机器
# ------------------------(max to 80 columns)-----------------------------------

import random
import datetime

# 教师生日年份范围 (2019-60)-(2019-24)
# 1959-1995

# 学生生日年份范围
# 高中2000-2003年

# 生日月的范围，不包含闰二月的29日


def generate_birthday(is_teacher):

    if is_teacher:
        yyyy = random.randint(1959, 1995)
    else:
        yyyy = random.randint(2000, 2003)

    mm = random.randint(1, 12)

    if mm == 2:
        dd = random.randint(1, 28)
    elif (mm == 4) or (mm == 6) or (mm == 9) or (mm == 11):
        dd = random.randint(1, 30)
    else:
        dd = random.randint(1, 31)

    # 创建一个datetime 型返回值
    birthday = datetime.date(yyyy, mm, dd)

    return birthday


# ---------------------------
if __name__ == '__main__':

    for idx in range(5):
        print(generate_birthday(True))
        print(generate_birthday(False))
