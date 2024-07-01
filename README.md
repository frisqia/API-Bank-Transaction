[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hMIDAFdr)


- users
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

----------------------------------------
- accounts
CREATE TABLE accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_type VARCHAR(255) NOT NULL,
    account_number VARCHAR(255) UNIQUE NOT NULL,
    balance DECIMAL(10,2) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-----------------------------------------
- transactions
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    from_account_id INT,
    to_account_id INT,
    amount DECIMAL(10,2) NOT NULL,
    type VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_account_id) REFERENCES accounts(id) ON DELETE CASCADE,
    FOREIGN KEY (to_account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

- select* from users;
- select* from accounts;
- select* from transactions;


# FLASK API FOR A BANKING APPLICATION
 - Develop a RESTfuk API: Implement a RESTful API using Flask that follow best practices of web development.
 - Connect to a MySQL database: Use SQLALchemy to connection to a MySQL Database and manage banking data effectively.
 - Implement secure user authentication : choose session-based or token-based authentication methods utilizing Flask-Login or Flask-JWT-Extended
 - Manage banking data:
    - Account Management:
        -  implement functionalities for creatin, updating , and managing user accounts(account type, balance, etc)
        - Integrate (account type, balance, etc.),
    - Transaction Management:
        - Implement functionalities for viewing, initiating, ang managing financial transactions(deposits, withdrawals, transfers).
        - Ensure secure transaction processing and maintain transaction history.
    - Write the API Documentation: Choose either OpenApi/Swagger, Postman, or Markdown formats.


    - ✅Build API using Flask
    - ✅Database Connection
    - ✅Flask Authentication
    - ✅API Documentation

    