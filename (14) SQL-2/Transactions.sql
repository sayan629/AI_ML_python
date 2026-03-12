CREATE DATABASE IF NOT EXISTS BANK;

USE bank;

CREATE TABLE account(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
balance DECIMAL(10,2)
);

INSERT INTO account(name, balance) VALUES
('Adam',500.00),
('Bob',300.00),
('Charlie',1000.00);

SELECT * FROM account;

  -- Transaction ------
-- Task: Transfer 50 rupees from Account 1 to Account 2 ---

START TRANSACTION;

UPDATE account SET balance = balance-50 WHERE id=1;
UPDATE account SET balance = balance+50 WHERE id=2;

COMMIT;

SELECT * FROM account;

		-- RollBack---

START TRANSACTION;

UPDATE account SET balance = balance-50 WHERE id=1;
UPDATE account SET balance = balance+50 WHERE id=2;
ROLLBACK;


START TRANSACTION;
UPDATE account SET balance = balance-50 WHERE id=1;
COMMIT;
UPDATE account SET balance = balance+50 WHERE id=2;
ROLLBACK;

START TRANSACTION;
UPDATE account SET balance = balance+1000 WHERE id=1;
SAVEPOINT after_wallet_topup;

UPDATE account SET balance = balance+10 WHERE id=2;
ROLLBACK TO after_wallet_topup;

COMMIT;