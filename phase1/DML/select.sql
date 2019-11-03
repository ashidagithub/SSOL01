# select all
SELECT rmgc20db.students.id,
    rmgc20db.students.name,
    rmgc20db.students.sex,
    rmgc20db.students.birthday
FROM rmgc20db.rmgc20db.students;

SELECT * FROM rmgc20db.rmgc20db.students;

# select - where
SELECT rmgc20db.students.id
FROM rmgc20db.students
WHERE rmgc20db.students.name = 'Lisa'
AND rmgc20db.students.sex = 1;
