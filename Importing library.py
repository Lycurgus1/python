# Using python library

from random import random
import math

print(random()) #Utilise random function from random library

float_num = 24.4
# Rounds float number
print(math.ceil(float_num))
# Rounds float number down
print(math.floor(float_num))
# Prints pi
print(math.pi)

def inches_to_cm(inch):
    cm = math.ceil(inch * 2.54)
    print("That converts to {} Centimetres".format(cm))

inches_to_cm(10)

# Same task but with user input
def conversion():
    text = input("Do you want to convert centimetres or inches? Enter C for cms and I for inches \n")
    if text.upper() not in ("C", "I"):
        print("Try again")
    else:
        number = float(input("Number to convert\n"))
        if text.upper() == "C":
            print("That converts to", int(number / 2.54), "centimetres.")
        elif text.upper() == "I":
            print("That converts to", int(number * 2.54), "inches.")



conversion()
