
/* 查询所有老师的信息 */
SELECT teacher_info.tid,
       teacher_info.class_code,
       teacher_info.t_name,
       teacher_info.t_sex,
       teacher_info.t_birthday,
       teacher_info.in_charge
FROM rmgc20_student.teacher_info;

/* 从数据表中随机抽取 n 条记录 */
SELECT tid
FROM teacher_info
ORDER BY rand()
LIMIT 5;


/* 查询某一门课的所有任课老师 */
SELECT course_info.c_name,
       teacher_course.tid,
       teacher_info.t_name
FROM course_info,
     teacher_course,
     teacher_info
WHERE course_info.cid = "GZSX0201"
  AND course_info.cid = teacher_course.cid
  AND teacher_course.tid = teacher_info.tid
