
from ragister_module import register_student
from search_module import search_student
from view_all_module import view_all
from delete_module import delete_student




while True:
    print("\n=========== STUDENT MANAGEMENT SYSTEM ===========")
    print("1. Register Student")
    print("2. Search Student")
    print("3. View All Students")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        register_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        view_all()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")