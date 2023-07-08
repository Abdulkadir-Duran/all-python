"""
you are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5

   = 1.6

  """

import math
#solution 1

def painting(wall_height, wall_width):
    result = (wall_height * wall_width) / 5
    return math.ceil(result)
height = int(input( "Enter the height of the wall \n"))
width = int(input("Enter the width of the wall \n"))
print("You'll need", painting(height, width), "cans of paint")

#solution 2
def calculator(h, w):
    cans = (h * w) / 5
    cans_up = math.ceil(cans)
    print(f"You'll need {cans_up} cans of paint")
height_wall = int(input("height \n"))
width_wall = int(input("width \n"))
calculator(h= height_wall, w=width_wall)


