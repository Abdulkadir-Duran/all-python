"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
"""
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
body_mass_index = round(weight / (height **2))

if body_mass_index < 18.5:
    print(f"Your BMI is {body_mass_index }, you are underweight.")
elif body_mass_index > 18.5 and body_mass_index < 25:

    print(f"Your BMI is  {body_mass_index}, you have a normal weight.")

elif body_mass_index > 25 and body_mass_index < 30:

    print(f"Your BMI is {body_mass_index}, you are slightly overweight.")
elif body_mass_index > 30 and body_mass_index < 35:

    print(f"Your BMI is {body_mass_index}, you are obese.")
else:
    print(f"Your BMI is {body_mass_index}, you are clinically obese.")
