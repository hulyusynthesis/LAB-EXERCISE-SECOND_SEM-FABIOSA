contacts = []

while True:
    print("\nList (1) Contact Manager")
    print("(1) Add a contact")
    print("(2) Remove a contact")
    print("(3) Show contacts")

    user = int(input("What are you trying to do today?\n"))

    if user == 1:
        print("Enter contact name:")
        contact = input("Type here: ")
        contacts.append(contact)
        print("Contact added!")

    elif user == 2:
        print("Which contact should we remove?")
        remove = input("Type here: ")
        if remove in contacts:
            contacts.remove(remove)
            print("Contacts:", contacts)
        else:
            print("Contact not found")

    elif user == 3:
        print("Contacts:", contacts)

    else:
        print("Invalid Input. Try Again")