# Nested Else If statment

# uses the keyword elif

# example use case
# If rain, than bring rain jacket, Elif snow, more layers, else bring t shirt

# you can also put a whole if else statement inside of another if else statement

# example of a Nested If else statement
age = int(input("How old are you? "))
if age >= 16:
    print("You may go to the concert")
    if age >= 20:
        print("Your ticket is $200")
    else:
        print("Your ticket is $100")
else:
    print("You may not go to the concert")