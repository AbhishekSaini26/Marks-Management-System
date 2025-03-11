import pymysql

# Connect to MySQL
conn = pymysql.connect(host="localhost", user="root", password="abhi", database="marks_db")
cursor = conn.cursor()

# Add Student Marks
def add_marks():
    name = input("Enter Student Name: ")
    subject = input("Enter Subject: ")
    marks = int(input("Enter Marks: "))
    cursor.execute("INSERT INTO students (name, subject, marks) VALUES (%s, %s, %s)", (name, subject, marks))
    conn.commit()
    print("Marks Added Successfully!")

# View All Student Marks
def view_marks():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if students:
        print("\nStudent Marks:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Subject: {student[2]}, Marks: {student[3]}")
    else:
        print("No records found.")

# Update Marks
def update_marks():
    student_id = int(input("Enter Student ID to Update: "))
    new_marks = int(input("Enter New Marks: "))
    cursor.execute("UPDATE students SET marks = %s WHERE id = %s", (new_marks, student_id))
    conn.commit()
    print("Marks Updated Successfully!")

# Delete Student Record
def delete_marks():
    student_id = int(input("Enter Student ID to Delete: "))
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    print("Record Deleted Successfully!")

# Main Menu
while True:
    print("\nMarks Management System")
    print("1. Add Marks")
    print("2. View Marks")
    print("3. Update Marks")
    print("4. Delete Record")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_marks()
    elif choice == "2":
        view_marks()
    elif choice == "3":
        update_marks()
    elif choice == "4":
        delete_marks()
    elif choice == "5":
        break
    else:
        print("Invalid Choice! Try Again.")

conn.close()
