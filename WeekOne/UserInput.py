print(f"User Input")

# User Input
# Upper case and lower case makes a difference

# upper(), lower(), title() and strip()
userResponse = input("Right me a sentence please ")
print(f"{userResponse.upper()}") # all upper case
print(f"{userResponse.lower()}") # all lower case
print(f"{userResponse.capitalize()}") # makes the first letter upper case the rest lower case
print(f"{userResponse.title()}") # all words start with an upper case
print(f"{userResponse.strip()}") # removes all starting and ending white space

# you can concatenate a bunch of these functions together like so
print(f"Concatenated versions: {userResponse.strip().lower()}")

#it can also be used like so
print("The cat went splat on the ground".upper())