# Master code from 02/07/2020

# Functions

# def greeting():
#     # pass # Pass creates function, allows to exist without error. Skips the function
#     return "Hello, World" # Returns anything you want function to return
#
#
# print(greeting()) # Function returns string which is then printed

# def add_values(x, y):
#     return x + y # Can return anything, string, int, int with operators.
#
# # print(add_values(1, 2))
#
# ## create a function with two args to return a subtraction of the 2 values given#
# def subtraction(x, y):
#     return x - y
#
# ## create a function with two args to return a division of the 2 values given
# def divison(x, y):
#     return x / y
#
# ## create a function with two args to return a remainder of  of the 2 values given
# def remainder(x, y):
#     return x % y
#
# ## create a function with two args to return a * of the 2 values given
# def multiplication(x, y):
#     return x * y
#
# ## Same but with user input
# def subtraction2():
#     x = int(input("Enter one number, please \n"))
#     y = int(input("Enter another, please \n"))
#     return x - y
#
# print(subtraction2())

## Multiple Arguments

# def my_first_function(*args):
#     # print(type(args))
#     for arg in args:
#         print("Wrong", arg)
#     return args # Return ends the function
#     # print("This function works,", args)
#
# my_first_function("jim", "Harry")

## Default values in functions
# def my_function(country = "Friesland"):
#     if country in ("Denmark"):
#         print("{} is a garbage country for garbage people".format(country))
#     else:
#         print("I am from", country)
#
# my_function("Denmark")
# my_function()

# # Raising exception



x = 6
if x < 5:
    raise Exception("Sorry no numbers below 5")
