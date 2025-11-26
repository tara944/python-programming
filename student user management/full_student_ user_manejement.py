list_deta = []


def register_student():
    student_dict = {}

    student_dict["id"] = int(input("Enter student id: "))
    student_dict["name"] = input("Enter student name: ")
    student_dict["address"] = input("Enter student address: ")
    student_dict["number"] = int(input("Enter phone number: "))

    qualification_list = []

    first_qualification = {
        "qualification": input("Enter first qualification: "),
        "passing_year": input("Enter passing year: ")
    }
    qualification_list.append(first_qualification)

    add_next = int(input("How much qualifications you want add: "))

    for i in range(add_next):
        qualification2 = {
            "qualification": input("Enter qualification: "),
            "passing_year": input("Enter passing year: ")
        }
        qualification_list.append(qualification2)

    student_dict["qualification"] = qualification_list
    list_deta.append(student_dict)

    print("Student Registered Successfully!")


def search_student():
    print("\nSearch by:")
    print("1. Phone Number")
    print("2. Qualification")

    choice = int(input("Enter choice: "))

    if choice == 1:
        num = int(input("Enter phone number: "))
        found = False

        for student in list_deta:
            if student["number"] == num:
                print("\n--- STUDENT FOUND ---")
                print(student)
                found = True

        if not found:
            print("No student found with this number.")

    elif choice == 2:
        quali = input("Enter qualification: ").lower()
        found = False

        for student in list_deta:
            for q in student["qualification"]:
                if q["qualification"].lower() == quali:
                    print("\n--- STUDENT FOUND ---")
                    print(student)
                    found = True

        if not found:
            print("No student found with this qualification.")


def view_all():
    if len(list_deta) == 0:
        print("No students registered.")
    else:
        print("\n=========== ALL STUDENTS ===========")
        for s in list_deta:
            print(s)


def delete_student():
    delete_id = int(input("Enter student ID to delete: "))
    found = False

    for student in list_deta:
        if student["id"] == delete_id:
            list_deta.remove(student)
            print("Student deleted successfully!")
            found = True
            break

    if not found:
        print("No student found with this ID.")


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