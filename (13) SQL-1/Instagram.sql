-- Create Database

CREATE DATABASE IF NOT EXISTS Instagram;

use instagram;

-- Create Table

CREATE TABLE user(
id INT,
age INT,
name VARCHAR(30) NOT NULL,
email VARCHAR(50) UNIQUE,
followers INT DEFAULT 0,
following INT,
CONSTRAINT CHECK (age>=13),
PRIMARY KEY (id)
);

CREATE TABLE post(
id INT PRIMARY KEY,
content VARCHAR(100),
user_id INT,
FOREIGN KEY (user_id) REFERENCES  user(id)
);


-- Insert Values in the table 

INSERT INTO user
(id,age,name,email,followers,following)
VALUES
(1,22,"Sayan","sayanpal191@gmail.com",827,343),
(2,22,"Samata", "samatanayek190@gmail.com",722,97),
(3,14,"Shreyas","shreyasnayek123@gmail.com",213,143),
(4,19, "Trisha","trishapal345@gmail.com", 101,261);

INSERT INTO user
(id,age,name,email,followers,following)
VALUES
(5,21,"Shlok","shlok1911@gmail.com",230,245),
(6,23,"Ruhon", "uixphuke.com",1405,595),
(7,13,"Shreyasi","shreyasipal1234@gmail.com",2134,145);

-- To print (id,name,age)

SELECT id, name, age FROM USER;

-- To print all 

SELECT * FROM USER;

-- Where Clause:- TO define some conditions

SELECT * FROM USER 
WHERE followers>=200;

SELECT name, followers 
FROM user 
WHERE followers>=200;

SELECT name, followers
 FROM user 
 WHERE age<19;

SELECT name, followers
FROM user 
WHERE age+1= 20;

SELECT name,age,followers 
FROM user 
WHERE age>19 AND followers>300;

SELECT name,age,followers
 FROM user
 WHERE age>15 OR followers>300;

SELECT name,age,followers
FROM user 
WHERE age BETWEEN 15 AND 19;

SELECT name,age,followers 
FROM user 
WHERE email IN("sayanpal191@gmail.com","samatanayek190@gmail.com","abc@gmail.com");

SELECT name,age,followers 
FROM user 
WHERE email NOT IN("sayanpal191@gmail.com","samatanayek190@gmail.com","abc@gmail.com");


-- Limit Clause

SELECT name , age, followers, following
FROM user
LIMIT 5;

-- Order By Clause

SELECT name,age
FROM user
ORDER BY followers ASC;


-- Aggregate Functions

SELECT Max(age)
FROM user;

SELECT Min(age)
FROM user;

SELECT Avg(age)
FROM user;

SELECT sum(followers)
FROM user;

SELECT count(age)
FROM user
WHERE age=22;

-- Group By Clause

SELECT age, count(id)
FROM user
GROUP BY age;

SELECT name, max(following)
FROM user
GROUP BY name;

SELECT age, max(followers)
FROM user
GROUP BY age;

-- HAVING CLAUSE

SELECT age, max(followers)
FROM user
GROUP BY age
HAVING max(followers)>400;

SELECT age, max(followers)
FROM user
GROUP BY age
HAVING max(followers)>400
ORDER BY age DESC;

-- Table Queries
-- UPDATE --

UPDATE user
SET followers = 300
WHERE age =19;

SET SQL_SAFE_UPDATES = 0;

SELECT * FROM user;

-- ALTER --
-- ADD Column --

ALTER TABLE user
ADD COLUMN city VARCHAR(30) DEFAULT "Delhi";

-- Drop Column --

ALTER TABLE user
DROP COLUMN city;

-- Rename Table --

ALTER TABLE user
RENAME TO InstaUser;

SELECT * from InstaUser;

ALTER TABLE InstaUser
RENAME TO user;

SELECT * from user;


-- Change Column(rename)

ALTER TABLE user
CHANGE COLUMN followers subs INT DEFAULT 0;

ALTER TABLE user
CHANGE COLUMN subs followers INT DEFAULT 0;


