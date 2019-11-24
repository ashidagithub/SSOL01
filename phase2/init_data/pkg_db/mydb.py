# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   学习通过类来使用数据库
# ------------------------(max to 80 columns)-----------------------------------


import mysql.connector


class MyDB():

    def __init__(self):
        self.__myconn = None
        self.__mycursor = None
        self.get_conn()
        self.get_cursor()
        return

    def get_conn(self):
        self.__myconn = mysql.connector.connect(
            host="localhost",
            database='fffff',
            user='student001',
            password='Rmgc+20-20',
            auth_plugin='mysql_native_password'
        )
        return self.__myconn

    def get_cursor(self):
        self.__mycursor = self.__myconn.cursor()
        return

    def commit(self):
        self.__myconn.commit()
        return

    @property  # 将 __myconn 对外部公开为只读属性
    def conn(self):
        return self.__myconn

    @property  # 将 __mycursor 对外部公开为只读属性
    def cursor(self):
        return self.__mycursor


if __name__ == '__main__':
    test_db = MyDB()

    tbl_name = 'course_info'
    sql = 'SELECT cid,c_name,introduce \
            FROM %s' % tbl_name

    test_db.cursor.execute(sql)
    myresult = test_db.cursor.fetchall() # fetchall() 获取所有记录
    print(myresult)

    print('-------------------')
    for row in myresult:
        print(row[0])


#myresult = [(cid, c_name, introduce),(cid, c_name, introduce),(cid, c_name, introduce)]
