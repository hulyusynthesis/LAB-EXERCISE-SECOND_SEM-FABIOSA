def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b

while True:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division\n[5] Exit Program")
    choice = int(input("Enter your choice [1-5]: "))

    if choice == 1:
        print(f"{num1:g} + {num2:g} = {add(num1, num2):g}")
    elif choice == 2:
        print(f"{num1:g} - {num2:g} = {subtract(num1, num2):g}")
    elif choice == 3:
        print(f"{num1:g} * {num2:g} = {multiply(num1, num2):g}")
    elif choice == 4:
        if num2 != 0:
            print(f"{num1:g} / {num2:g} = {divide(num1, num2):g}")
        else:
            print("Error! Cannot divide by zero!")
    elif choice == 5:
        print("\nExiting Program...")
        break
    else:
        print("\nInvalid choice, Please Try Again!")
