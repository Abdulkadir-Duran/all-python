
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

#add function
def add(n1, n2):
    return n1 +n2
#subtraction  function
def diff(n1, n2):
    return  n1 - n2
#multplication  function
def multply(n1, n2):
    return n1 * n2
#division  function
def diivde(n1, n2):
    return  n1 / n2
operations = {"+": add,
              "-" : diff,
              "*": multply,
              "/": diivde
              }
def calculation_recussion():
    print(logo)
    number1 = int(input("What is your first number"))
    for operation in operations:
        print(operation)
        should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above")
        number2 = int(input("What is your next number"))
        calculation = operations[operation_symbol]
        answer = calculation(number1, number2)
        print(f"{number1 } {operation_symbol} {number2} = {answer}")
        continue_choice = input(f"type 'y' to continue with  {answer} or type 'n' to start new calculator")
        if continue_choice == 'y':

            number1 = answer
        else:
            should_continue = False
            calculation_recussion()
calculation_recussion()













