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

## Using python library

from random import random
import math

# print(random()) #Utilise random function from random library

# float_num = 24.4
# # Rounds float number
# print(math.ceil(float_num))
# # Rounds float number down
# print(math.floor(float_num))
# # Prints pi
# print(math.pi)

# def inches_to_cm(inch):
#     cm = math.ceil(inch * 2.54)
#     print("That converts to {} Centimetres".format(cm))
#
# inches_to_cm(10)

## Same task but with user inpurt
# def conversion():
#     text = input("Do you want to convert centimetres or inches? Enter C for cms and I for inches \n")
#     if text.upper() not in ("C", "I"):
#         print("Try again")
#     else:
#         number = float(input("Number to convert\n"))
#         if text.upper() == "C":
#             print("That converts to", int(number / 2.54), "centimetres.")
#         elif text.upper() == "I":
#             print("That converts to", int(number * 2.54), "inches.")
#
#
#
# conversion()

## Default values in functions
# def my_function(country = "Friesland"):
#     if country in ("Denmark"):
#         print("{} is a garbage country for garbage people".format(country))
#     else:
#         print("I am from", country)
#
# my_function("Denmark")
# my_function()

## Create a calculator with a class. Should have methods to +, -, /, *, %
## Create class object
## Run class
# class Python_Calulcator:
#
#     def add_values(self, num1, num2): # Self key word refers to the class
#         return num1 + num2
#
#     def subtract_values(self, num1, num2):
#         return num1 - num2
#
#     def divide_values(self, num1, num2):
#         return num1 / num2
#
#     def multiply_values(self, num1, num2):
#         return num1 * num2
#
#     def remainder_values(self, num1, num2):
#         return num1 % num2
#
# print(Python_Calulcator.subtract_values("Jim", -1, 3))
#
# object = Python_Calulcator()
#
# print(object.add_values(1, 2))

## Object orientated python

## Inheritance, polymorhpism, encapsulation, abstraction

class Dog:
    amimal_kind = "Canine" # Class variable

    # Init intalizes class
    # Give/find name and color for dog
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        return "woof, woof"

# create a methods inside for sleep, breath, run, eat

    # Encapsulation. This creates a private method. Abstraction is a expansion on this
    def __sleep(self):
        return "zzzzz"

    # Pas enables this function without error
    def breath(self):
        pass

    # Inheritance. This refers to creating sub classes, but run is using is a
    # previously define attribute
    def run(self):
        return "Come back, {}".format(self.name)

    # Polymorphism. Here the sub class method overrides the methods in the
    # parent class when appropriate. It first searches it its own class, then
    # in its inherited class
    def eat(self):
        print("{} is eating fast".format(self.__class__.__name__))

class Retriever(Dog):
    def eat(self):
        print("Retriever is eating slowly")

class Labrador(Dog):
    pass

jim = Dog("Canine", "White") # Creating object of our class
peter = Dog("peter", "Brown")

# print(jim.name)

## Testing encapsulation
# print(peter.__sleep())

## Testing inheritance
# print(peter.run())

## Testing polymorphism
print()