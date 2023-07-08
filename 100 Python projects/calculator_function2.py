logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
    return n1 +n2
#subtraction  function
def diff(n1, n2):
    return  n1 - n2
#multplication  function
def multply(n1, n2):
    return n1 * n2
#division  function
def divide(n1, n2):
    return  n1 / n2
def calculation():
    print(logo)
    print("welcome to the calculator")
    num1 = float(input("What is your first number? "))
    print("""
    +
    -
    *
    /""")
    while True:
        operation_symbol = input("pick an operation")
        if operation_symbol == '+':
            num2 = float(input("What is your next number? "))
            result = add(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")

            if input(f"type 'y' to continue with {result } or type 'n' to start new calculator ") == 'y':
                num1 = result
            else:
                False
                calculation()
        elif operation_symbol == '-':
            num2 = float(input("What is your next number? "))
            result = diff(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")

            if input(f"type 'y' to continue with {result } or type 'n' to start new calculator ") == 'y':
                num1 = result
            else:
                False
                calculation()
        elif operation_symbol == '*':
            num2 = float(input("What is your next number? "))
            result = multply(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")


            if input(f"type 'y' to continue with {result } or type 'n' to start new calculator ") == 'y':
                num1 = result

            else:
                False
                calculation()
        elif operation_symbol == '/':
            num2 = float(input("What is your next number? "))
            result = diff(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {result}")

            if input(f"type 'y' to continue with {result} or type 'n' to start new calculator ") == 'y':
                num1 = result


            else:
                False
                calculation()


        else:
            print("please select valid operation from the list")

calculation()


