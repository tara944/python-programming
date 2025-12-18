from student_crud.student_detail import Crud


def main():
    c = Crud()

    while True:
        print("\n1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            id = int(input("Enter id: "))
            name = input("Enter name: ")
            c.create(id, name)

        elif choice == "2":
            c.read()

        elif choice == "3":
            id = int(input("Enter id: "))
            name = input("Enter new name: ")
            c.update(id, name)

        elif choice == "4":
            id = int(input("Enter id: "))
            c.delete(id)

        elif choice == "5":
            print("Bye ")
            break

        else:
            print("Wrong choice")


if __name__ == "__main__":
    main()
