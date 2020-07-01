# String slicing

greeting_welcome = "Cheese world" # H is the 0th character. Indexing starts at 0.
print(greeting_welcome[3]) # Gets 4th character from string
print(greeting_welcome[-1]) # Gets last character from string
print(greeting_welcome[-5:]) # Gets 1st character to last
x = greeting_welcome[-5:]
print(x)

# Strip - remove spaces

remove_white_space = "remove spaces at end of string "
print(len(remove_white_space))
print(remove_white_space.strip()) # Removes spaces at end of string
print(len(remove_white_space.strip())) # Length can bee seen to go down
