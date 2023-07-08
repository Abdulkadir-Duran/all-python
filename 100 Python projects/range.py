
total  = 0
for number in range(1, 101):
    total += number
print(total)

#exercise

"""

You are going to write a program that calculates the sum of all the
 even numbers from 1 to 100. Thus, the first even 
number would be 2 and the last one is 100:
"""
#way 1
sum_numbers =0
for num in range(1, 101):
    if num % 2 == 0:
        sum_numbers += num
print(sum_numbers)

#way  2
even_sum = 0
for number in range(2, 101, 2):
  # print(number)
  even_sum += number
print(even_sum)