import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Update Student")
    print("6. Remove All Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # Add Student
    if choice == 1:

        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        department = input("Enter student department: ")

        cursor.execute(
            "INSERT INTO students(name, age, department) VALUES (?, ?, ?)",
            (name, age, department)
        )

        conn.commit()
        print("Student Added Successfully")

    # Display Students
    elif choice == 2:

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if len(students) == 0:
            print("No student found")

        else:
            print("\n----- Student Records -----")

            for student in students:
                print(f"""
ID         : {student[0]}
Name       : {student[1]}
Age        : {student[2]}
Department : {student[3]}
----------------------------
""")

    # Search Student
    elif choice == 3:

        search_name = input("Enter student name to search: ")

        cursor.execute(
            "SELECT * FROM students WHERE name = ?",
            (search_name,)
        )

        student = cursor.fetchone()

        if student:
            print(f"""
ID         : {student[0]}
Name       : {student[1]}
Age        : {student[2]}
Department : {student[3]}
""")
        else:
            print("Student not found")

    # Remove Student by Name
    elif choice == 4:

        remove_name = input("Enter student name to remove: ")

        cursor.execute(
            "DELETE FROM students WHERE name = ?",
            (remove_name,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student removed successfully")
        else:
            print("Student not found")

    # Update Student by Name
    elif choice == 5:

        old_name = input("Enter student name to update: ")

        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        new_department = input("Enter new department: ")

        cursor.execute(
            """
            UPDATE students
            SET name = ?, age = ?, department = ?
            WHERE name = ?
            """,
            (new_name, new_age, new_department, old_name)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully")
        else:
            print("Student not found")

    # Remove All Students
    elif choice == 6:

        confirm = input("Are you sure? (yes/no): ")

        if confirm.lower() == "yes":

            cursor.execute("DELETE FROM students")

            # Reset ID counter
            cursor.execute(
                "DELETE FROM sqlite_sequence WHERE name='students'"
            )

            conn.commit()

            print("All students removed successfully")

        else:
            print("Operation cancelled")

    # Exit
    elif choice == 7:

        conn.close()
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")