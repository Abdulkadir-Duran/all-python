
quiz = {
    "Question1":{
        "question": "What is the capital city of Hiran",
        "Answer": "Baladweyne"

    },
    "Question2": {
        "question": "What is the capital city of Mudug",
        "Answer": "Galkio"
    },
    "Question3": {
        "question": "What is the capital city of Banadir",
        "Answer": "Mogadishu"
    },
    "Question4": {
        "question": "What is the capital city of Bari",
        "Answer": "Bossaso"
    },
    "Question5": {
        "question": "What is the capital city of lower Juba",
        "Answer": "Kismayo"

    }
}
score = 0
for key, value in quiz.items():
    print(value["question"])
    answer = input("What is your answer?\n")
    if answer == value["Answer"].lower():
        print("Correct")
        score += 1
        print("your is score is", score)
    else:
        print("Wrong")
        print(score)
print("you got:", score, "out of 5 correctly")
print(f"your percentage is: {int(score/5 *100)}% ")
