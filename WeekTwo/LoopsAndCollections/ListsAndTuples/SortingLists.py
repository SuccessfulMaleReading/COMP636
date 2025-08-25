#Sorting Lists

my_list = ['mat', 'Sat', 'hat', '5.2', 'free', 'bat', 'MAT']

# to sort the list above we use the function

# sort()
# This sorts insides the list and discards the original order

# sorted()
# This keeps the original but returns a sorted copy

# sort() defaults to ascending

my_list.sort()
print(my_list)
# this will sort the original list into ascending order

my_list.sort(reverse=True)
print(my_list)
# this will sort everything into descending order

# for Tuples you cannot use sort() because you can't change a tuple, but you can use sorted to create a copy
my_tuple = (5, 3, 7)
new_order = sorted(my_tuple)
print(my_tuple)
print(new_order)