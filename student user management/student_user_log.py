list_deta=[]

def ragister_studefdent():
    student_dict={}   

    student_dict["id"]=int (input("enter student id:"))
    student_dict["name"]=input("enter student name")
    student_dict["address"]=input("enter student address")
    student_dict["number"]=input("enter student number")

    qualification_list=[]
    qualificationq1={
        "qualification":input("enter your qualification:"),
        "passing_yeare":input("enter passing yeare:")   
    }
    qualification_list.append(qualificationq1)

    next=int(input("enter how much qualification you want add"))

    for i in range(next):
        qualificationq2={
          "qualification":input("enter your qualification:"),
        "passing_yeare":input("enter passing yeare:")     
        }
        qualification_list.append(qualificationq2)
        student_dict["qualificaton"]=qualification_list
        list_deta.append(student_dict)

        print("student ragister sussfully")

def search_student():
    print("\n chose one")
    print("1.number")
    print("2.qualification")

    choice=int(input("enter choice"))

    if choice==1:
        num=int(input("enter number:"))
        found=False

        for student in list_deta:
            if student["number"]==num:
                print("\n=====student found=====",)
                print(student)
                found=True
        if not found:
            print("student not found")

    elif choice==2:
        quali=input("enter qualification")
        found=False

        for student in list_deta:
            for q in student["qualificaton"]:
                if q["qualification"].lower()==quali.lower():
                    print("=====student found=======") 
                    print(student)
                    found=True
        if not found:
            print("student not found")

def view_all():
    if len(list_deta)==0:
        print("no student register")
    else:
        print("print all studemnt")
        for s in list_deta:
            print(s)
            



                
        

