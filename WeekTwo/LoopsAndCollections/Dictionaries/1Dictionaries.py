# Like lists and tuples, a dictionary is a collection of items, but each 'item' is a key:value pair.
#
# We create a dictionary using curly braces { }
# We separate each key and its value with a colon ' : '

# example
students = { 100456:"Alice Liddell", 100543:"Xavier Smith", 100478:"Amrita Singh" }

# KEYS

# each key must be unique
# - if a key is repeated, the existing value will be replaced with the new value
# - A key's data type can be:  int , float , str, tuple, NoneType.
# - keys are immutable (cannot be changed)

# Value
# Values can be repeated, and can be any data type.
# example
dictionaryType = {'roof':'grey', 'door':'grey', 'storeys':2, 'double-glazed':True }

# Get a value using its key.  Use either [ ], or .get( )

print(students[100456])
print(students.get(100456))
# both should work the same

students = {100456:"Alice Liddell", 100543:"Xavier Smith", 100478:"Amrita Singh"}
all_names = students.values()
print(f"Names are {all_names}")
students.update({100456:"Bob Downe"})
print(f"Names are {all_names}")



