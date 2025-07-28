#Simple print statement
print("Hello World")
name = "Andrew"  # Creates a variable named 'name' and the value assigned is "Andrew"
print(f"Hello {name}")  #the f allows for variables to be added to the print statement using {}

#How inputs are added
myName = input("What is your name? ") # input() takes in user input from the console and stores it into the myName variable
print(f"Hello {myName}")


# example below shows adding int() tells the string that the input is an integer
numOne = int(input("Enter the first number: ")) # this breaks if a number is not entered
numTwo = int(input("Enter the second number: "))
numSum = numOne + numTwo
print(f"The sum of your numbers is {numSum}")

print("welcome to", numOne, "!")  # commas adds a space to the start and end
print("welcome to" + numOne + "!")  # + does not att spaces in between

