def add(n1, n2):
    return n1 + n2
def diff(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
def calc():
    operations = {"+": add, "-": diff,
                  "*": multiply, "/": divide}

    for operation in operations:
        print(operation)

    number1 = int(input("Enter the first number "))

    while True:
        user_choice = input("Please choose an operation from the list obove ")

        number2 = int(input("what is  the next number "))
        calculation = operations[user_choice]
        answer = calculation(number1, number2)

        print(f"{number1} {user_choice} {number2} = {answer}")
        next_continue = input(f"Type 'y' to continue with {answer} or type 'n' to start new calculator ")
        if next_continue == "y":
            number1 = answer
        else:
            False
            calc()

calc()




























