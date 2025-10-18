CREATE DATABASE IF NOT EXISTS transactions_db;
USE transactions_db;

CREATE TABLE customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  customer_id VARCHAR(64) UNIQUE NOT NULL,
  name VARCHAR(255),
  email VARCHAR(255)
);

CREATE TABLE accounts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  account_id VARCHAR(64) UNIQUE NOT NULL,
  customer_id VARCHAR(64) NOT NULL,
  account_type VARCHAR(50),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  txn_id VARCHAR(128) UNIQUE NOT NULL,
  account_id VARCHAR(64) NOT NULL,
  amount DECIMAL(12,2) NOT NULL,
  currency VARCHAR(10) NOT NULL,
  txn_time DATETIME NOT NULL,
  status VARCHAR(50),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);
