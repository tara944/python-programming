students = []

def register_student():
    student = {}
    student["id"] = int(input("Enter ID: "))
    student["name"] = input("Enter Name: ")
    student["address"] = input("Enter Address: ")
    student["phone"] = input("Enter Phone: ")

    students.append(student)
    print("\nStudent Registered Successfully!")
