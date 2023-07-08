#local scope
# local variables are those which are defined inside the function and they can only be accessible inside the function

enemy = 1

def increase_enemies():
  enemy = 2
  print(f"enemies inside function: {enemy}")

increase_enemies()
print(f"enemies outside function: {enemy}")

# Global scope
#local variables are those which are defined outside  the function and they can both be accessible inside the function

enemies = 2
def increase_enemies():

  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#How to modify a global variable with "global"
enemy = 1

def increase_enemies():
 global enemy
 enemy +=4
 print(f"enemies inside function: {enemy}")

increase_enemies()
print(f"enemies outside function: {enemy}")

