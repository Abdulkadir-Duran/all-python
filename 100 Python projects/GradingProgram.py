
"""
You have access to a database of student_scores in the format of a dictionary. The keys in student_scores
are the names of the students and the values are their exam scores.

Write a program that converts their scores to grades. By the end of your program, you should have a
new dictionary called student_grades that should contain student names for keys and their grades for
values. The final version of the student_grades dictionary will be checked.

DO NOT modify lines 1-7 to change the existing student_scores dictionary.

DO NOT write any print statements.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"


"""
student_scores = {
    "Abdi": 80,
    "ali": 99,
    "Fuad": 75,
    "john" : 68


}
sudent_grade = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90 and score <= 100:
        sudent_grade[student] = "Execellnt"
    elif score > 80 and score <= 90:
        sudent_grade[student]  = "good"
    elif score > 70 and score <= 80:
        sudent_grade[student]  = "medium"
    elif score > 60 and score <= 70:
        sudent_grade[student]  = "pass"
    else:
        sudent_grade[student]  = "fail"
print(sudent_grade)



