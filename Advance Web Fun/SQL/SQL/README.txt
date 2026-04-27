# MySQL Workbench CRUD Assignment

## Description
In this assignment, I used MySQL Workbench to connect to my localhost database and practice basic CRUD operations.

CRUD means:
- Create
- Read
- Update
- Delete

## Database Used
users_schema

## Table Used
users

## SQL Commands Used

```sql
USE users_schema;

INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ('Jalil', 'Wasaya', 'wasaya.jalil@gmail.com', NOW(), NOW());

SELECT * FROM users;

UPDATE users
SET email = 'newemail@gmail.com'
WHERE id = 1;

DELETE FROM users
WHERE id = 1;