# LAB EXERCISE 8: Contact Book Using Lists and Dictionaries

contacts = []

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Display 6.Exit")
    try:
        ch = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if ch == 1:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts.append({"name": name, "phone": phone})

    elif ch == 2:
        name = input("Enter name: ")
        for contact in contacts:
            if contact["name"] == name:
                print(contact)
                break
        else:
            print("Contact not found")

    elif ch == 3:
        name = input("Enter name: ")
        for contact in contacts:
            if contact["name"] == name:
                contact["phone"] = input("New phone: ")
                print("Contact updated.")
                break
        else:
            print("Contact not found")

    elif ch == 4:
        name = input("Enter name: ")
        old_count = len(contacts)
        contacts = [c for c in contacts if c["name"] != name]
        print("Contact deleted." if len(contacts) < old_count else "Contact not found.")

    elif ch == 5:
        print(contacts)

    elif ch == 6:
        break
    else:
        print("Invalid choice.")
