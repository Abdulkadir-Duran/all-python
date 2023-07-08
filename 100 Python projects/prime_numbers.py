
def prime_checker(number):
    for num in range(2, number ):
        if number % num == 0:
            print("it is not a prime number")

    else:
        print("it is a prime")
prime = int(input("Enter the number you want to check \n"))
prime_checker(number= prime)


number = int(input("enter the number \n"))
factorial = 1
if number < 2:
    print(f"the factorial of {number} is {factorial}")
else:
    for num in range(1, number +1):
        factorial = factorial * num
    print(f"the factorial of {number} is {factorial}")





