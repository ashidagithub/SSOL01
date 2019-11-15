INSERT INTO rmgc20_student.teacher_info
(tid,class_code,t_name,t_sex,t_birthday,in_charge)
VALUES
(<{tid: }>,
<{class_code: }>,
<{t_name: }>,
<{t_sex: }>,
<{t_birthday: }>,
<{in_charge: }>);


UPDATE rmgc20_student.teacher_info
SET
tid = <{tid: }>,
class_code = <{class_code: }>,
t_name = <{t_name: }>,
t_sex = <{t_sex: }>,
t_birthday = <{t_birthday: }>,
in_charge = <{in_charge: }>
WHERE tid = <{expr}>;
