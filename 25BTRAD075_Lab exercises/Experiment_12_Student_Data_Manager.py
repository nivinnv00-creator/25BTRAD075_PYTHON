# LAB EXERCISE 12: Student Data Manager Using Files

FILE_NAME = "students.txt"

while True:
    print("\n1.Add 2.Display 3.Search 4.Update 5.Delete 6.Exit")
    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if ch == 1:
        roll = input("Roll number: ")
        name = input("Name: ")
        mark = input("Mark: ")
        with open(FILE_NAME, "a") as f:
            f.write(roll + "," + name + "," + mark + "\n")

    elif ch == 2:
        try:
            with open(FILE_NAME, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No student records found.")

    elif ch in (3, 4, 5):
        roll = input("Enter roll number: ")
        try:
            with open(FILE_NAME, "r") as f:
                records = f.readlines()
        except FileNotFoundError:
            records = []

        found = False
        updated_records = []

        for record in records:
            data = record.strip().split(",")
            if data[0] == roll:
                found = True
                if ch == 3:
                    print(record.strip())
                    updated_records.append(record)
                elif ch == 4:
                    name = input("New name: ")
                    mark = input("New mark: ")
                    updated_records.append(roll + "," + name + "," + mark + "\n")
                # For delete, the matching record is not added.
            else:
                updated_records.append(record)

        if ch in (4, 5):
            with open(FILE_NAME, "w") as f:
                f.writelines(updated_records)

        if not found:
            print("Record not found")

    elif ch == 6:
        break
    else:
        print("Invalid choice.")
