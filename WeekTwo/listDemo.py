# Tuple List
fruits = ["orange","strawberry","banana","apple","blueberry","kiwifruit"]
#print(fruits)

# how to sort
sortedFruits = sorted(fruits) # sorted() | sorts the list in typical alphabetical order
#print(sortedFruits)

sortedFruits = sorted(fruits, reverse = True) # sorted(var, reverse=True) sorts in reverse
#print(sortedFruits)

fruits.sort() # this function modifies the list directly
#print(fruits)

print(fruits[0]) # prints out what is in the specific index in the list

# range

rangeValues = range(6)
print(rangeValues)

for value in rangeValues:
    print(value)

for value2 in rangeValues:
    print(fruits[value2])