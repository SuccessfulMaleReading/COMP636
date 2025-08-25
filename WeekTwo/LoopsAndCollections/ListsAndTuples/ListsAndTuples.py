# List and Tuples are a convenient way for us to store multiple items in just one place

# example
# friend1 = "Andrew"
# friend2 = "Jordan"
# friend3 = "Jethro"

# instead of many variables we can create one variable  that stores all the names

# List and Tuples are similar
# both allow storage of multiple items in a variable
# both allow us to access the whole variable
# both ordered

# but...

# lists can be changed - add more items, remove items, edit an individual item, reorder items
# tuples cannot be changed

friends = ["Jethro","Jordan","Larry"]

# index() can grab the index value of an item in a list or tuple
print(f"Jordan's position in the list is {friends.index('Jordan')}")
# which should return with 1

