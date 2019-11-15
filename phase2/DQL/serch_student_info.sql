/* 统计每个班级的人数 */
SELECT class_code, count(*) FROM rmgc20_student.student_info
group by class_code
order by class_code;
