# combining separate lists into one nested tuple

# use the zip() function

itemID = [1, 2, 3, 4, 5]
fruit = ['feijoa', 'apples', 'bananas', 'cherries', 'mango']
price = [0.85, 0.35, 0.45, 7.99, 5.75]
country = ['NZ','NZ','Ecuador','NZ','India']

# existing lists ^
list_of_tuples = list( zip(itemID,fruit,price,country) )

nestedList = list( zip(itemID,fruit,price,country) )
print(nestedList)

# combining list of lists into list of tuples
my_items = [ ['Bob','Anita','Jack'], ['orange','banana'],['cheese','milk','fish','noodles'] ]

#convert each inner list into a tuple
new_list = list(map(tuple, my_items))
print(new_list)