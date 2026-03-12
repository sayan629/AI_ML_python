USE orderdetails;

SELECT * FROM customers;
SELECT * FROM orders;

-- Views in SQL --
CREATE VIEW view1 AS
SELECT customer_id , name FROM customers;

SELECT * FROM view1;

CREATE VIEW view2 AS
SELECT c.customer_id,  c.name , o.order_id
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

 