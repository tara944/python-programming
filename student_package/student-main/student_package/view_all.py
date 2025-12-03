from student_package.register import students

def view_all():
    print("\n===== ALL STUDENTS =====")
    for st in students:
        print(st)
