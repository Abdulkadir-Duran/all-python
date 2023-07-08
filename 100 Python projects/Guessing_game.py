
logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
from random import randint
Hard_level = 5
Mediam_level = 7
Easy_level = 10
answer = randint(1, 100)

def chech_answer(computer_answer, user_guess, attempts):
    if user_guess > computer_answer:
        print("Too high, please try again")
        return attempts - 1
    elif user_guess < computer_answer:
        print("too low, please try again")
        return attempts - 1
    else:
        print(f"Congratulations you won the game, the answer is {computer_answer}")
def game_level():
    level = input("""The game has 3 level. 'easy' to choose the easy level, type 'hard' to choose the hard level or type 
    'medium' to choose the medium level """)
    if level == 'easy':
        return Easy_level
    elif level == 'mediam':
        return Mediam_level
    elif level == 'hard':
        return Hard_level
    else:
        print("Invalid level")
def game():
    print(logo)
    print("Welcome to the number guessing game.")
    print("I am thinkling of a number between 1 and 100.")

    turns = game_level()
    guess = 0
    while guess != answer:
        print(f" You have {turns} attempts.")
        guess = int(input("Guess a number the between 1 and 100 to get sectet number "))
        turns = chech_answer(computer_answer= answer, user_guess= guess, attempts= turns)
        if turns == 0:
            print("You lose the game")
            print(f"The answer is {answer}")
            break

game()














