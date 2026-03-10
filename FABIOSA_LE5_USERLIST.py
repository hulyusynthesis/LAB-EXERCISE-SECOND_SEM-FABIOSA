users = []

while True:
        print("\n=== MAIN MENU ===")
        print("1. Show User")
        print("2. Add User")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("\nWaiting for User Input: ")
        
        if choice == "1":
            if users:
                print("\nUsers:", users)
            else:
                print("\nNo users found.")
        
        elif choice == "2":
            user = input("Enter New User: ")
            users.append(user)
            print(f"User '{user}' added. Current users: {users}")
        
        elif choice == "3":
            update = input("Which User shall we update: ")
            if update in users:
                index = users.index(update)
                new_value = input("Enter New User: ")
                users[index] = new_value
                print(f"User updated. Current users: {users}")
            else:
                print(f"User '{update}' not found.")
        
        elif choice == "4":
            remove = input("Which User shall be removed? ")
            if remove in users:
                users.remove(remove)
                print(f"User '{remove}' removed. Current users: {users}")
            else:
                print(f"User '{remove}' not found.")
        
        elif choice == "5":
            print("Exiting...")
            exit()
        
        else:
            print("Invalid choice. Please try again.")
    
    
