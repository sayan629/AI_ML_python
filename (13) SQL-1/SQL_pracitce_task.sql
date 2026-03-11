CREATE DATABASE IF NOT EXISTS College;
use college;

CREATE TABLE Teacher(
	id INT PRIMARY KEY,
    name VARCHAR(30),
    subject VARCHAR(50),
    salary INT
);

INSERT INTO teacher
(id, name, subject, salary)
VALUES
(23, "ajay", "math", 50000),
(47, "bharat","english",60000),
(18, "chetan", "chemistry",45000),
(9, "divya", "physics",75000);

SELECT * FROM teacher;

SELECT * FROM teacher  
WHERE salary>55000;

ALTER TABLE teacher
CHANGE COLUMN salary ctc INT;

UPDATE teacher 
SET ctc= ctc + ctc * 0.25;

SET SQL_SAFE_UPDATES=0;

ALTER TABLE teacher
ADD COLUMN City VARCHAR(50) DEFAULT "Gurgaon";

ALTER TABLE teacher
DROP COLUMN ctc;


-- Practice Task 2 --

CREATE TABLE student(
rollno INT PRIMARY KEY,
name VARCHAR(30),
city VARCHAR(30),
marks INT
);

INSERT INTO student
(rollno,name,city,marks)
VALUES
(110,"adam", "Delhi",76),
(108,"bob","Mumbai",65),
(124, "casey","Pune",94),
(112,"dhuke","Pune", 86);

SELECT * FROM student;

SELECT * FROM student
WHERE marks>75;

SELECT DISTINCT city
FROM student;

SELECT avg(marks)
FROM student;

ALTER TABLE student
ADD COLUMN grade VARCHAR(2);

UPDATE student
SET grade ="O"
WHERE marks>=80;

UPDATE student
SET grade ="E"
WHERE marks>=70 AND marks<80;

UPDATE student
SET grade ="A"
WHERE marks>=60 AND marks<70;

SELECT * FROM student;