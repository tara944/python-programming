from student_package.register import students

def search_student():
    sid = int(input("Enter ID to search: "))
    found = False

    for st in students:
        if st["id"] == sid:
            print("\n===== STUDENT FOUND =====")
            print(st)
            found = True
            break

    if not found:
        print("Student Not Found!")
        
