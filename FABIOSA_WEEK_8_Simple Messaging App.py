try:
    f = open("message.txt", "x")
    f.close()
    print("File 'message.txt' created successfully!!!")
except FileExistsError:
    print("Error: 'message.txt' already exists.")

while True:
    print("\n Welcome to the messaging App!.\n")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        message = input("Enter your message: ")
        try:
            f = open("message.txt", "a")
            f.write(message + "\n")
            f.close()
            print("Message sent!")
        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        try:
            f = open("message.txt", "r")
            messages = f.read()
            f.close()
            if messages == "":
                print("No messages yet.")
            else:
                print("\nMessages:")
                print(messages)
        except Exception as e:
            print("Error:", e)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")