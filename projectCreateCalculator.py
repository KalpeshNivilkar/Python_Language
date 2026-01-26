def cal():
    print("Calculator!")

    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))

    print("Choices: sum, sub, div, mul")
    choice = input("Enter your choice: ").lower()

    if choice == "sum":
        print("Result:", num_1 + num_2)

    elif choice == "sub":
        print("Result:", num_1 - num_2)

    elif choice == "mul":
        print("Result:", num_1 * num_2)

    elif choice == "div":
        if num_2 != 0:
            print("Result:", num_1 / num_2)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")
cal()