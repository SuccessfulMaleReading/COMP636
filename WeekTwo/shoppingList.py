# using lists

# if we didn't have a list, we would have to manually list out everything as so
# item1 = input("Item 1 on Shopping List")
# item2 = input("ITem 2 on Shopping List")
# item3 = input("Item 3 on Shopping List")
#
# print(f"{item1}\n{item2}\n{item3}")

items = []

# you can append things to the list instead

# items.append("Milk")
# items.append("Bananas")
# items.append("Coffee")


# this allows the user to input a item and save it into the list
# items.append(input("Please enter item name: "))

# Using WHILE we can make this more user-friendly

#initiate the loop

# initiate one, because if the user enters no straight away
# it does not initiate the while statement
itemCheck = input("Please enter your item (enter 'no' to quit): ")

while itemCheck.strip() != "no" and itemCheck.strip() != "No" and itemCheck.strip() != "NO":
    items.append(itemCheck)
    itemCheck = input("Please enter your item (enter 'no' to quit): ")

print(items)

# code above avoids white space error and also checks for different variations of no

item2 = []
count = 0
itemCheck2 =input("Please enter your item (enter 'no' to quit): ")

while itemCheck2.strip().upper() != "NO":
    item2.append(itemCheck2)
    itemCheck2 = input("Please enter your item (enter 'no' to quit): ")
    count += 1
print(item2)
print(count)

# code above makes things a lot more readable
# the while statement concatenates functions together so that it strips white space and also converts text to all upper
# case. So now you don't have to type out all the extra AND statements

for userResponse in item2:
    print(userResponse)

a = 0
# two different options - however the for loop in this case is much more simple
while a != count:
    print(item2[a])
    a += 1

# PRINTING OUT A LIST

# For loop


