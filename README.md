# Student Management System

A simple Student Management System developed using **Python** and **SQLite**. This project demonstrates CRUD (Create, Read, Update, Delete) operations with a database.

## Features

* Add new students
* Display all student records
* Search students by name
* Update student details
* Remove a student
* Remove all students
* Store data permanently using SQLite database

## Technologies Used

* Python
* SQLite
* SQL Queries

## Project Structure

```text
student-management-system/
│
├── main.py
├── database.py
├── student.db
└── README.md
```

## Database Operations

### Create

Add a new student using:

```sql
INSERT INTO students(name, age, department)
VALUES (?, ?, ?)
```

### Read

Display and search student records using:

```sql
SELECT * FROM students
```

### Update

Modify existing student details using:

```sql
UPDATE students
SET name=?, age=?, department=?
WHERE name=?
```

### Delete

Remove student records using:

```sql
DELETE FROM students WHERE name=?
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/student_management_system.git
```

2. Navigate to the project folder:

```bash
cd student_management_system
```

3. Create the database and table:

```bash
python database.py
```

4. Run the application:

```bash
python main.py
```

## Learning Outcomes

Through this project, I learned:

* Python programming fundamentals
* SQLite database connectivity
* SQL queries (INSERT, SELECT, UPDATE, DELETE)
* CRUD operations
* Git and GitHub project management

## Author

**Surya P G**

GitHub: https://github.com/SURYA-P-G
