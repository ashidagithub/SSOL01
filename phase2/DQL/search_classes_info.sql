/* 获取有班级的总数 */
SELECT count(*) FROM classes_info


SELECT classes_info.class_code,
    classes_info.tid,
    classes_info.class_name,
    classes_info.class_grade,
    classes_info.class_no
FROM rmgc20_student.classes_info;
