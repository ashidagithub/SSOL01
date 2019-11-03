
CREATE TABLE rmgc20db.students (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(20) NOT NULL,
  sex int(11) NOT NULL,
  birthday date NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
