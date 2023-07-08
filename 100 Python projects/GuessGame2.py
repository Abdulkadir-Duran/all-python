
from random import randint
Hard_level = 5

Easy_level = 10
answer = randint(1, 100)
print("Welcome to the number guessing game.")
print("I am thinkling of a number between 1 and 100.")
level = input("type 'hard' or type 'easy' ")
turns = 0
if level == 'hard':
    print(f" you have {Hard_level} attemps")
    guess = 0
    while guess != answer:
        guess = int(input(" Make a guess"))
        Hard_level -= 1
        print(f" you have {Hard_level} attemps")
        if guess > answer:

            print("too high")
            if Hard_level == 0:
                break
        elif guess < answer:
            print("Too low ")
            if Hard_level == 0:
                print(f"You lose, the answer is {answer}")
                break

        else:
            print(f"You won, the answer is {answer}")
else:
    print(f" you have {Easy_level} attemps")
    guess = 0
    while guess != answer:
        guess = int(input("Make a guess"))
        Easy_level -= 1
        print(f" you have {Easy_level} attemps")
        if guess < answer:
            print("too low")
            if Easy_level == 0:
                print(f"you loose the answer is {answer}")
                break
        elif guess > answer:
            print("too high")

            if Easy_level == 0:
                print(f"you loose the answer is {answer}")
                break
        else:
            print("you won ")










