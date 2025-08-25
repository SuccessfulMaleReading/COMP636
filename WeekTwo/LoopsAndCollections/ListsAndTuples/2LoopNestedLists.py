# fruit contains 3 items
fruit = [ 'apple' , 'orange' , 'mango' ]

# charges contains 3 items
charges = [ 13.5 , 'standard fee' , 7 ]

# my_items contains 3 items (but each item is another list)
my_items = [ ['Bob','Anita','Jack'] , ['orange','banana'] , ['cheese','milk','fish','noodles'] ]
my_tuple = ( ('Bob','Anita','Jack') , ('orange','banana') , ('cheese','milk','fish','noodles') )

# Looping overs Lists of Lists

# example

for eachList in my_items:
    print(eachList)
# this list loops over each list in the list

for eachList in my_items:
    for eachItem in eachList:
        print(eachItem)
# This list loops over each item in each list


# The above combined
for eachList in my_items:
    print(f"--- {eachList} ---")
    for eachItem in my_items:
        print(f" - {eachItem}")

for item in my_tuple:
    for listItem in item:
        print(listItem)