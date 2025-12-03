from ragister_module import list_deta

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
