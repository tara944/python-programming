from student_package.register import students

def delete_student():
    choice= int(input("enter student id to delete"))
    found=False
    
    for st in students:
        if st["id"]==choice:
            
            students.remove(st)
            print("student deleted ")
            found=True
            break
        
    if not found:
        print("student not found")
    
