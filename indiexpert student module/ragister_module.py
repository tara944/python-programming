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
