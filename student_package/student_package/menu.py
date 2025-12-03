from student_package.register import register_student
from student_package.search import search_student
from student_package.view_all import view_all
from student_package.delete import delete_student

def menu():
    while True:
        print("\n=========== STUDENT MENU ===========")
        print("1. Register Student")
        print("2. Search Student")
        print("3. View All Students")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            search_student()
        elif choice== "3":
            view_all()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")
