# Nested Lists

# fruit contains 3 items
fruit = [ 'apple' , 'orange' , 'mango' ]

# charges contains 3 items
charges = [ 13.5 , 'standard fee' , 7 ]

# my_items contains 3 items (but each item is another list)
my_items = [ ['Bob','Anita','Jack'] , ['orange','banana'] , ['cheese','milk','fish','noodles'] ]

print(fruit[1]) # should print orange
print(charges[0]) # should print 13.5
print(my_items[0]) # should print ['Bob','Anita','Jack']
print(my_items[0][2]) # should print Jack
print(my_items[2][3]) # should print noodles

