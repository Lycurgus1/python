# print("Hello, World")

# Create variable

# x = 10  # Integer
# y = 3.6  # Float
# z = "Test"  # String
#
# result = x + y

# print(result)

# Built in method called type

# print(type(x))

# Cannot combine string and float. So cast int into string first

# Will not work
# print(y + z)

# print(str(y) + z)

# Getting input
# x = input("Enter name")
# print( x )

# Overriding value

# z = "New word"
# print(z)
# z = "New new"
# print(z)

# Exercise User Details

# Create variable called first_name and last_name
first_name = input("Enter first name here \t")
last_name = input("Enter last name here \t")

# # Create variable called age

age = int(input("Enter age \t"))

# Create variable named address

address = input("Enter address \t")

# Prompt user for information

# Create a variable named full_name and display

full_name = ('{} {}'.format(first_name, last_name))
print(full_name, age, address)
