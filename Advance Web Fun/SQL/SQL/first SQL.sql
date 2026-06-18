#CREATE DATABASE users_schema;
#PRIMARYusersUSE users_schema;
# CREATE TABLE users (
#    id INT PRIMARY KEY AUTO_INCREMENT,
#    first_name VARCHAR(50) NOT NULL,
#    last_name VARCHAR(50) NOT NULL,
#    email VARCHAR(100) NOT NULL,
#    created_at DATETIME NOT NULL,
#    updated_at DATETIME NOT NULL
# );


INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ('Jalil', 'Wasaya', 'wasaya.jalil@gmail.com', NOW(), NOW());

SELECT * FROM users;


UPDATE users
SET email = 'new@email.com'
WHERE id = 1;


DELETE FROM users
WHERE id = 2;

SELECT * FROM users;
