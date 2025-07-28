print("IF STATEMENTS")

#
#   This program will take in a users age
#   and print out activities they are able to
#   do for, example, join social media
# or drive
#

# The users name
name = ""
# the users age
age = 0
# above is initializing variables

name = input("Please enter your name: ")
# this code takes in a float and converts it into and integer
# which is what we want in this case for age
age = int(float(input("Please enter your age: ")))

# constraints for this program
# activities
# Must be over 13 years old
# Must register for a driving license must be 16 or older

if age >= 13:
    print("You can join social media")
    if age >= 16:
        print("You can register for a learner license")
    else:
        print("You can register for a learner licenese when you turn 16")
else:
    print(f"Sorry {name}, you can't join social media")