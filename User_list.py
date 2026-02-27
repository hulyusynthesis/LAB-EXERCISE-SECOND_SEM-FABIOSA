print("=== MAIN MENU ===")
show = print("\n1. Show User.")
add =print("\n2. Add User. ")
upd = print("\n3. Update User. ")
dlt = print("\n4. Delete User. ")
ext = print("\n5. Exit. ")


choice = input("Waiting for User Input: ")
if(choice == add):
   user = input("Enter New User: ")

elif(choice == upd):
   update = input("Which User shall we update: ")
   if update in user:
      index = user.index(update)
      new_value = input("Enter New User: ")
      user[index] = new_value
      print(user)

elif(choice == dlt):
   remove = input("Which User shall be removed? ")
   if remove in user:
      user.remove(remove)
      print(user)

elif(choice == ext):
   exit()
   
   
