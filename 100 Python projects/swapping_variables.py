"""
Write a program that switches the values stored in the variables a and b.

Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for
different inputs. e.g. any value of a and b.
"""

a = int(input("a: "))
b = int(input("b:"))
temp = a
a = b
b = temp
print("a:", a)
print("b: ", b)
name = len(input("what is your name? "))
new_name = str(name)
print("your name has " + new_name + "characters")
print(f" your name has {name} characters")