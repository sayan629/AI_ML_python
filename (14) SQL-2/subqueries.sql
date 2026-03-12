USE orderdetails;

SELECT * FROM customers;
SELECT * FROM orders;

	-- Subquery --
    -- With Where
    
SELECT *
FROM orders
WHERE amount>(
SELECT AVG(amount)
FROM orders
);

	-- With SELECT

SELECT name,
	(
	SELECT COUNT(*)
    FROM orders o
    WHERE o.customer_id=c.customer_id
    ) as order_count
FROM customers c;

	-- With Form 

SELECT
	summary.customer_id,
    summary.avg_amount
FROM (
		SELECT
			customer_id,
            AVG (amount) AS avg_amount
		FROM orders
        GROUP BY customer_id
        ) AS summary;