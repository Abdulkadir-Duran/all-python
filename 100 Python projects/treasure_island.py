print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road = input('you are at a cross road. Where do you want to go? type "left" or "right" ')
if road == "left":
    lake = input('''you come to a lake. this is island in the middle of the lake. Type "wait" to wait for a boat. Type swim to swim accross ''')

    if lake == "wait":
        color = input("""you arrive at the island unharmed. there is a house with 3 doors. 
        One red, one yellow and one blue. which color do you choose """)
        if color == "blue":
            print("you enter a room of beasts.  Game over.")
        elif color == "red":
            print("It's a room full of fire. Game over")
        else:
            print("You found the treasure! You win!")
    else:
        print("You get attacked by an angry trout. Game over")
else:
    print("You fell into a hole. Game Over. Game over")