
"""
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall
person and a short person both weigh
 the same amount, the short person is usually more overweight.
"""
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
body_mass_index = int(weight) / float(height) ** 2
print(round(body_mass_index, 1))