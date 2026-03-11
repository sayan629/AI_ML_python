CREATE DATABASE IF NOT EXISTS EmployeeDetails;

USE EmployeeDetails;

CREATE TABLE Employee (
EmpID INT PRIMARY KEY,
FirstName VARCHAR(30),
LastName VARCHAR(30),
Department VARCHAR(15),
salary INT,
HireDate DATE
);

INSERT INTO Employee VALUES
(101,'Alice','Johnson','IT',6500,'2020-03-15'),
(102,'Mark','Rivera','HR',4800,'2019-07-22'),
(103,'Sophia','Lee','Finance',7200,'2021-01-10'),
(104,'Daniel','Kim','IT',5800,'2018-11-05'),
(105,'Emma','Brown','Marketing',5300,'2022-04-18'),
(106,'Liam','Patel','Finance',6900,'2020-09-29'),
(107,'Olivia','Garcia','HR',4600,'2017-06-30'),
(108,'Noah','Thompson','IT',7500,'2023-02-12'),
(109,'Ava','Martinez','Marketing',5100,'2019-12-02'),
(110,'Ethan','Davis','Finance',8000,'2016-05-14');

SELECT * FROM Employee;

SELECT FirstName, LastName, salary
from employee;

SELECT * from employee
WHERE department="IT";

SELECT * from employee
WHERE salary>6000;

SELECT DISTINCT Department
FROM employee;

SELECT *
FROM employee
WHERE FirstName LIKE 'A%';

SELECT * from employee
WHERE salary BETWEEN 4000 AND 7000;

SELECT AVG(salary) AS Average_Salary
FROM Employee;

SELECT Department, COUNT(*) AS Employee_Count
FROM employee
GROUP BY Department
HAVING COUNT(*)>3;