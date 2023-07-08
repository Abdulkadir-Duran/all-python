"""
def factorial(number):
    factorial_number =1
    if number > 1:
        for n in range(1, number +1):
            factorial_number = factorial_number * n
        print(f"the factoial of {number} is {factorial_number}")
    elif number < 0:
        print(f" {number}  has no factorial because it is negative nuber")
    else:
        print(f"the factoial of {number} is {factorial_number}")
"""
def gcd(a, b):
    num = 1

    for n in range(1, a +1):
        if a % n == 0 and b % n == 0:
            num = n
    return num



number1 = int(input("Enter the first number \n"))
number2 = int(input("Enter the second number \n"))
print(f"the GCD of {number1} and {number2} is {gcd(number1, number2)}")

