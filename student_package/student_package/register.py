students=[]

def register_student():
    student={}
    student["id"]=int(input("enter student id :"))
    student["name"]=input("enter your name :")
    student["address"]=input("enter the address :")
    student["phone"]=int(input("enter phone number :"))
    
    student.append(student)
    print("student registeration sussfully!")
    
    