
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#Add an item to the end of the list
fruits.append('grape')
print(fruits)
#Insert an item at a given position. The first argument is the index of the element before which to insert,
fruits.insert(3, 'mango')
print(fruits)
#Return the number of times x appears in the list.
print(fruits.count('banana'))
#get the position of x in the list
print(fruits.index('orange'))

#sort lists
fruits.sort()
print(fruits)

print(fruits)
#delete all the lists
fruits.clear()
print(fruits)
