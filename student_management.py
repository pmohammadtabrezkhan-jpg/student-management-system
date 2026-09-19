import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    branch = input("Enter Branch: ")

    maths = float(input("Enter Maths marks: "))
    python = float(input("Enter Python marks: "))
    english = float(input("Enter English marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "branch": branch,
        "marks": {
            "maths": maths,
            "python": python,
            "english": english
        }
    }

    students.append(student)
    save_students()

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students available.")
        return

    for student in students:
        print("\n-------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Branch:", student["branch"])

        print("Maths:", student["marks"]["maths"])
        print("Python:", student["marks"]["python"])
        print("English:", student["marks"]["english"])


def search_student():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            print("\nStudent Found")
            print("-------------------------")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            print("Maths:", student["marks"]["maths"])
            print("Python:", student["marks"]["python"])
            print("English:", student["marks"]["english"])

            return

    print("Student not found.")


def update_student():
    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found")

            name = input("Enter new name: ")
            age = input("Enter new age: ")
            branch = input("Enter new branch: ")

            student["name"] = name
            student["age"] = age
            student["branch"] = branch

            save_students()

            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            students.remove(student)
            save_students()

            print("Student deleted successfully!")
            return

    print("Student not found.")


def calculate_average():
    student_id = input("Enter Student ID: ")

    for student in students:

        if student["id"] == student_id:

            maths = student["marks"]["maths"]
            python = student["marks"]["python"]
            english = student["marks"]["english"]

            total = maths + python + english
            average = total / 3

            print("\nStudent:", student["name"])
            print("Total Marks:", total)
            print("Average:", average)

            if average >= 90:
                print("Grade: A")

            elif average >= 75:
                print("Grade: B")

            elif average >= 60:
                print("Grade: C")

            elif average >= 40:
                print("Grade: D")

            else:
                print("Grade: F")

            return

    print("Student not found.")


students = load_students()


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_average()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")