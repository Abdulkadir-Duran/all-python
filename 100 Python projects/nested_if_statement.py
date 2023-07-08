
print("welcome to the order")
height = int(input("Enter your height in cm "))
if height >= 180:
    print("you can order")
    age = int(input("Enter your age"))
    if age <=10:
        print("please pay $7")
    else:
        print("pay $12")
else:
    print("sorry, youn have to grow taller before you order")