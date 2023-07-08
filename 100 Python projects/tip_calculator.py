print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
people = int(input("How many peole to split the bill? "))
percentage = float(input("What percentage would you likr to give? "))
amount_percentage = (percentage / 100) * bill
total = amount_percentage + bill
split = total / people
rounded_split = round(split, 3)
print(f"Each person should pay: ${rounded_split}")