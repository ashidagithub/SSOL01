# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.10

# Description:
#   创建一个产生教师工号的机器
# ------------------------(max to 80 columns)-----------------------------------

import random

# 教师工号命名规则
# 入职年度（4位）+'-'+流水号（5位）
# Sample: 2005No003


def generate_worker_number():

    # 入职年度 介于 1985-2019年之间
    yyyy = random.randint(1985, 2019)
    # 流水号 介于 0-999 之间
    serial_number = random.randint(0, 99999)

    # 工号
    num = '%d-%05d' % (yyyy, serial_number)

    return num


# ---------------------------
if __name__ == '__main__':
    for idx in range(5):
        print(generate_worker_number())
