x = 10
y = 11

print(x == y) # Returns false as x not equal to y
print(x != y) # Is x not equal to y?
print(x > y) # Is x more than y. Also could use <=
print(x < y) # Is x less than y. Also could use >=

# Real life example. Checks if age is right
age = 17

print(age >= 18)

# Double vs single quotes. Both work, though double is better.

print("Max's Brie")
print('Max's Brie') # Apostrophe in string throws off interpreter
print('Max\'s class is cool') # Slash cancels out apostrophe, so it can be used

# Strings

greeting_welcome = 'Hiya' # H is the 0th character. Indexing starts at 0.
print(len(greeting_welcome)) # Finds length of string

# Concanenation

welcome_user = input("Enter name here \t")
greeting = "How are you"
print(greeting + ', ' + welcome_user + '?') # Concetanation
