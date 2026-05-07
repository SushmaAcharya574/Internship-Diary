import pickle
import os

FILE_NAME = "students.dat"

# Create Student Class
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.name}, Marks: {self.marks}")


# Add Student
def add_student():
    f = open(FILE_NAME, "ab")
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    
    s = Student(roll, name, marks)
    pickle.dump(s, f)
    f.close()
    print("Student added successfully!\n")


# Display All Students
def display_students():
    try:
        f = open(FILE_NAME, "rb")
        print("\nStudent Records:")
        while True:
            s = pickle.load(f)
            s.display()
    except EOFError:
        f.close()
    except FileNotFoundError:
        print("No records found.\n")


# Search Student
def search_student():
    roll = int(input("Enter Roll No to search: "))
    found = False

    try:
        f = open(FILE_NAME, "rb")
        while True:
            s = pickle.load(f)
            if s.roll == roll:
                print("Student Found:")
                s.display()
                found = True
                break
    except EOFError:
        f.close()

    if not found:
        print("Student not found.\n")


# Update Student
def update_student():
    roll = int(input("Enter Roll No to update: "))
    updated = False

    try:
        f = open(FILE_NAME, "rb")
        temp = open("temp.dat", "wb")

        while True:
            s = pickle.load(f)
            if s.roll == roll:
                print("Enter new details:")
                s.name = input("Enter Name: ")
                s.marks = float(input("Enter Marks: "))
                updated = True
            pickle.dump(s, temp)

    except EOFError:
        f.close()
        temp.close()

    os.remove(FILE_NAME)
    os.rename("temp.dat", FILE_NAME)

    if updated:
        print("Record updated successfully!\n")
    else:
        print("Student not found.\n")


# Delete Student
def delete_student():
    roll = int(input("Enter Roll No to delete: "))
    deleted = False

    try:
        f = open(FILE_NAME, "rb")
        temp = open("temp.dat", "wb")

        while True:
            s = pickle.load(f)
            if s.roll != roll:
                pickle.dump(s, temp)
            else:
                deleted = True

    except EOFError:
        f.close()
        temp.close()

    os.remove(FILE_NAME)
    os.rename("temp.dat", FILE_NAME)

    if deleted:
        print("Record deleted successfully!\n")
    else:
        print("Student not found.\n")


# Menu
def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


# Run Program
menu()
