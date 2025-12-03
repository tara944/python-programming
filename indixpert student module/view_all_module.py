from ragister_module import list_deta
def view_all():
    if len(list_deta) == 0:
        print("No students registered.")
    else:
        print("\n=========== ALL STUDENTS ===========")
        for s in list_deta:
            print(s)
