# find the gcd of two numbers
#function without retuen value
def gcd_1(a, b):
    num = 1

    for n in range(1, a +1):
        if a % n == 0 and b % n == 0:
            num = n
    print(f"the GCD of {a} and {b} is {num}")




number1 = int(input("Enter the first number \n"))
number2 = int(input("Enter the second number \n"))
gcd_1(a= number1, b= number2)



#function with return value
def gcd_2(a, b):
    num = 1

    for n in range(1, a +1):
        if a % n == 0 and b % n == 0:
            num = n
    return num



number1 = int(input("Enter the first number \n"))
number2 = int(input("Enter the second number \n"))
print(f"the GCD of {number1} and {number2} is {gcd_2(number1, number2)}")
