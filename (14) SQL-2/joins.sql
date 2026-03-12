CREATE DATABASE IF NOT EXISTS orderDetails;
USE orderDetails;

CREATE TABLE customers (
customer_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO customers VALUES
(1,'Alice','Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie' , 'Bangalore'),
(4, 'David' , 'Mumbai');

CREATE TABLE orders(
order_id INT PRIMARY KEY,
customer_id INT,
amount INT
);

INSERT INTO orders VALUES
(101,1,500),
(102,1,900),
(103,2,300),
(104,5,700);

SELECT * FROM customers;
SELECT * FROM orders;

-- inner Join

SELECT *
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id;

SELECT c.customer_id, o.order_id, c.name
FROM customers c
INNER JOIN orders o
ON c.customer_id=o.customer_id;

 -- Left Join --
  
 SELECT *
 FROM customers c
 LEFT JOIN orders o
 ON c.customer_id=o.customer_id;
  
 -- Right Join --
  
 SELECT *
 FROM customers c
 RIGHT JOIN orders o
 ON c.customer_id=o.customer_id;
 
 -- Outer Join --
  
 SELECT *
 FROM customers c
 LEFT JOIN orders o
 ON c.customer_id=o.customer_id
 UNION
 SELECT *
 FROM customers c
 RIGHT JOIN orders o
 ON c.customer_id=o.customer_id;
 
 -- Cross Join --
 
 SELECT *
 FROM customers
 CROSS JOIN orders;
 
  -- SELF Join --
 
 SELECT *
 FROM customers as A
 JOIN customers as B
 ON A.customer_id= B.customer_id;
 
 -- Left Exclusive Join --
 
 SELECT *
 FROM customers as A
 LEFT JOIN orders as B
 ON A.customer_id = B.customer_id
 WHERE B.customer_id is NULL;
 
 -- Right Exclusive Join --
 
SELECT *
FROM customers as A
RIGHT JOIN orders as B
ON A.customer_id = B.customer_id
WHERE A.customer_id is NULL;
 
 
 