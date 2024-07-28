CREATE DATABASE finance_tracker;
USE finance_tracker;

CREATE TABLE Categories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(255)
);

CREATE TABLE Transactions (
    TransactionID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryID INT,
    TransactionDate DATE,
    Description VARCHAR(255),
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

INSERT INTO Categories (CategoryName) VALUES
('Groceries'),
('Rent'),
('Utilities'),
('Entertainment'),
('Travel'),
('Dining Out'),
('Income');

