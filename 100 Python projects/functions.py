# painting calculator
#Write your code below this line 👇
import math

import math
def paint_calc(height, width, cover):
    cans = (height * width) / cover
    cans_up = math.ceil(cans)
    print(f"you will need {cans_up}")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# prime number checker

def prime_check(prime_number):
    for number in range(2, prime_number ):
        if prime_number % number == 0:
            print("it is not a prime number")

    else:
            print("it is a prime number")
prime = int(input("Enter the number to check"))
prime_check(prime_number= prime)
