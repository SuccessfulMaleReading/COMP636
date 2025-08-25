# Copying and Slicing Lists

# suppose you have the code
age = 44
sheep = 44
dumplings = age
# you now have the value 44 stored three times

# Lists don't work like this
# When we assign a list to a variable, the variable does not store the list.
# The variable stores a reference to the list (in other words, the variable stores the address of wherever the list is being stored)

# example
my_pets = ["dog","lizard","dog","dog","hen"]
animals = my_pets # animals points to (refers to) the same list as my_pets
animals[1] = "horse" # change item[1] in the list that animals refers to
print(f"my_pets are now {my_pets}")

# you can see from the example above, both variables refer to the same list

# How to have a separate copy of a list
# we can properly copy a list bby slicing
# code example
# [start:stop before]

my_list = ["mat","sat","hat",5.2,"free",False,"bat",7,"MAT"]
a_slice = my_list[2:6]
# The slice is assigned a new list containing the slice of values from my_list[2] to my_list[5]. That is
# NOT including my_list[6]

b_slice = my_list[:3]
# this takes all items 0, 1, 2

c_slice = my_list[0:]
# this takes all items from 0
print(f"{a_slice}")
print(f"{b_slice}")
print(f"{c_slice}")


# what if you want to copy every second item from the list
# example
d_slice = my_list[0:8:2]