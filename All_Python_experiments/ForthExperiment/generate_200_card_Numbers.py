import random

Card_ids = []#Define an empty list

for i in range(1, 201): ##Generate a number from 1 to 200
    s = '6102009%0.3d' % i #Set the first few to 6102009, the last three digits of 001 mode
    Card_ids.append(s) #Add elements to the defined empty list
Card_dict = {}.fromkeys(Card_ids,'redhat')
print('card number\tpassword') ##Generate the dictionary, the key with different bits corresponds to the same value, and from
for k in Card_dict:
    random_password = random.choice(Card_ids)
    print( random_password, Card_dict[k])




