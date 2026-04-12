def show_balance(balance):
    # balance
    print(f"\n  Current Balance: P{balance:.2f}")


def withdraw(balance):

    # loop
    while True:

        try:
            # ask the user how much they want to withdraw
            amount = float(input("\nEnter withdrawal amount: P"))

            # check if the user entered zero or a negative number
            if amount <= 0:
                print("Error: Please enter a positive amount.")
                continue

            # check if the user does not have enough balance
            if amount > balance:
                raise ValueError("Insufficient funds")

            # subtract the amount from the balance
            balance -= amount
            print(f"Successfully withdrew P{amount:.2f}")
            show_balance(balance)

            # send the updated balance back to the main function
            return balance

        except ValueError as e:

            # check what kind of error happened
            if "Insufficient funds" in str(e):
                # tell the user they dont have enough money
                print(f"\nError: Insufficient funds!")
                print(f"You tried to withdraw P{amount:.2f} "
                      f"but only P{balance:.2f} is available.")
            else:
                # this runs when the user types letters instead of a number
                print("\nError: Invalid input! Please enter a valid number.")

            # give the user options after an error instead of closing the program
            print("\nWhat would you like to do?")
            print("[1] Re-enter withdrawal amount")
            print("[2] Check current balance")
            print("[3] Exit")

            option = input("\nEnter option: ")

            # go back to the withdrawal prompt
            if option == "1":
                continue
            # show the balance then go back to the withdrawal prompt
            elif option == "2":
                show_balance(balance)
                continue
            # close the program
            elif option == "3":
                print("\nThank you for using the ATM. Goodbye!")
                exit()
            # if the option is not valid just go back to the withdrawal
            else:
                print("Invalid option. Returning to withdrawal.")
                continue


def main():

    # show the title of the program
    print("=" * 40)
    print("        SIMPLE ATM SYSTEM")
    print("=" * 40)

    # set the starting balance to 5000
    balance = 5000.00
    show_balance(balance)

    # this loop keeps the menu running until the user chooses to exit
    while True:
        print("\n--- MAIN MENU ---")
        print("[1] Withdraw")
        print("[2] Check Balance")
        print("[3] Exit")

        choice = input("\nEnter choice: ")

        # go to the withdraw function and save the new balance
        if choice == "1":
            balance = withdraw(balance)
        # show the current balance
        elif choice == "2":
            show_balance(balance)
        # exit the program
        elif choice == "3":
            print("\nThank you for using the ATM. Goodbye!")
            break
        # if the input is not 1 2 or 3 just show an error and loop back
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()