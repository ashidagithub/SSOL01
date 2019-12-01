
tbl_name ='xxxx'

sql = 'INSERT INTO %s ' % tbl_name
#sql = 'INSERT INTO %s ' % tbl_name

sql += '(tid,class_code,t_name,t_sex,t_birthday,in_charge) '
sql += 'VALUES ( '
sql += ') '
'''
sql += '"%s","%s","%s",%d,"%s",%s' % (tid, class_code, name, sex, birthday, in_charge)
'''
print(sql)
