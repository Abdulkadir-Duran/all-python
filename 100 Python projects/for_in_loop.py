
"""
You are going to write a program that calculates the average student height from a List of heights.
"""
student_heights = input("the list of the students").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])
total = 0
for height in student_heights:
    total += height
students_number= 0
for number in student_heights:
    students_number += 1
avg = total // students_number
print(avg)














