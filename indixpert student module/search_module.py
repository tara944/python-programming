
from ragister_module import list_deta

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