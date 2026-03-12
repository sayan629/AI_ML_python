USE orderdetails;

CREATE TABLE accounts(
	account_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10,2),
    branch VARCHAR(50)
);

INSERT INTO accounts VALUES
(1, 'Adam',500.00,'Mumbai'),
(2, 'Bob',300.00,'Delhi'),
(3,'Charlie',700.00,'Bangalore'),
(4,'David',1000.00,'Noida');

select * from accounts;

-- Index in SQL (Single Column) --

CREATE INDEX idx_branch ON accounts(branch);

SHOW INDEX FROM accounts;


-- Index in SQL (Multiple Column/Composite Index) --

CREATE INDEX idx2 ON accounts(branch,balance);

SHOW INDEX FROM accounts;

DROP INDEX idx2 ON accounts;


		-- Stored Procedures --
DELIMITER $$ 

CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
	SELECT balance
    FROM accounts
    WHERE account_id=acc_id;
END $$

DELIMITER ;

CALL check_balance(1);
CALL check_balance(2);

DROP PROCEDURE IF EXISTS check_balance;

-- --- ----

DELIMITER $$ 

CREATE PROCEDURE check_balance(IN acc_id INT, OUT bal DECIMAL (10,2))
BEGIN
	SELECT balance INTO bal
    FROM accounts
    WHERE account_id=acc_id;
END $$
DELIMITER ;


CALL check_balance(1,@balance);
SELECT @balance;




