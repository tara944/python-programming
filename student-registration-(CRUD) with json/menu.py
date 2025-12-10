from student_registration import register
from student_registration import view_all_student
from student_registration import search_student
from student_registration import delete_student


while True:
    print("\n----- Student Management -----")
    print("1 - Register Student")
    print("2 - View All Students")
    print("3 - Search Student by ID")
    print("4 - Delete Student")
    print("5 - Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        view_all_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")
