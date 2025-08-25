# sorting list of lists

tuple_list = [
    (1,'zulu',53),
    (4,'yellow',51),
    (3,'x-ray',57),
    (2,'yob',60)
    ]

# create a new copy of the list
new_tuple_list = sorted(tuple_list)
# [(1,'zulu',53), (2,'yob',60), (3,'x-ray',57), (4,'yellow',51)]

# lets say you want to sort this list by the second item in each tuple (e.g. index 1)

# we use the lamda function
# lambda atuple : atuple[1]
print(new_tuple_list)
new_tuple_list = sorted(new_tuple_list, key=lambda atuple: atuple[1])
print(new_tuple_list)

print("-------------------------------------")

# specify more than one sort key
# sometimes you want 2 or more sort keys
# example:  For example, to sort a list of students by family name, but where several students have the same family name then sort them within family name by first name.
#
# Specify the keys to be returned from your lambda function as a tuple.
# For example:
students=[
    (100444,'Annie','Lee',67),
    (100321,'Eve','Brown',95),
    (100477,'Dom','Xu',49),
    (100480,'Bob','Brown',78),
    (100491,'Will','Brown',60),
    (100411,'Kaia','Lee',78)
    ]
students.sort( key=lambda x: (x[2],x[1]) )

# The first-level key is [2], the family names, so this gives Brown, Brown, Brown, Lee, Lee, Xu.
# But, where there are duplicate family names (eg, 3x Brown) the second-level key of [1] is then applied, to get Bob Brown then Eve Brown then Will Brown.
# The same goes for family name Lee, Annie first then Kaia.
