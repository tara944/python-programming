from student_package.register import students

def delete_student():
    sid = int(input("Enter ID to delete: "))
    found = False

    for st in students:
        if st["id"] == sid:
            students.remove(st)
            print("\nStudent Deleted Successfully!")
            found = True
            break

    if not found:
        print("Student Not Found")
