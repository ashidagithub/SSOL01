-- SELECT 所有列
SELECT rmgc20db.students.id,
    rmgc20db.students.name,
    rmgc20db.students.sex,
    rmgc20db.students.birthday
FROM rmgc20db.students;

-- （不推荐）SELECT 所有列
SELECT * FROM rmgc20db.students;

-- 添加 WHERE 语句的 SELECT
SELECT rmgc20db.students.id
FROM rmgc20db.students
WHERE rmgc20db.students.name = 'Lisa'
AND rmgc20db.students.sex = 1;

-- 查询数据库的记录总数
SELECT COUNT(*) FROM rmgc20db.students
