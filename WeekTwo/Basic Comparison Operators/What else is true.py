# any string can evaluate as true, even if its not a boolean variable
# anything accept an empty string ""


# for example if we ask the user to enter her name via an input() function
# we could have it so that something different is displayed instead (e.g. they click enter without entering anything)

name = input("what is your name? ")
# ask the user for input and save users in put into the variable name
if name:
    print(f"Hello, {name}")
else:
    print("Hello No Name")
# If the name variable contains anything at all it is evaluates to true, so the first print statement will execute
# If the name variable is empty "" that evaluates to false, so the else print statement will execute

# handy use case, this can be used to detect if a list item has a value stored in it

# all things empty will evaluate to false including lists, boolean: false and the key value None
