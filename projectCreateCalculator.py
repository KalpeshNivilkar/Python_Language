

def cal(num_1, num_2):
    add = 0
    subt = 0
    division = 0
    multiplication = 0
    print("Calculator!")
    num_1 = int(input("Enter the first number : "))
    num_2 = int(input("Enter the second number :"))
    print("choices: SUM,SUB,DIV,MUL")
    choice = input("Enter your choice :")
    finalChoice = choice.lower

    if choice == sum:
        return num_1 + num_2


