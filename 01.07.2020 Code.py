## Data types
## Strings
## Concenation

# x = 10
# y = 11
#
# print(x == y) # Returns false as x not equal to y
# print(x != y) # Is x not equal to y?
# print(x > y) # Is x more than y. Also could use <=
# print(x < y) # Is x less than y. Also could use >=

## Real life example. Checks if age is right
# age = 17
#
# print(age >= 18)

## Double vs single quotes. Both work, though double is better.

# print("Max's Brie")
# print('Max's Brie') # Apostrophe in string throws off interpreter
# print('Max\'s class is cool') # Slash cancels out apostrophe, so it can be used

## Strings

# greeting_welcome = 'Hiya' # H is the 0th character. Indexing starts at 0.
# print(len(greeting_welcome)) # Finds length of string

## Concanenation

# welcome_user = input("Enter name here \t")
# greeting = "How are you"
# print(greeting + ', ' + welcome_user + '?') # Concetanation

## String slicing

# greeting_welcome = "Cheese world" # H is the 0th character. Indexing starts at 0.
# print(greeting_welcome[3]) # Gets 4th character from string
# print(greeting_welcome[-1]) # Gets last character from string
# print(greeting_welcome[-5:]) # Gets 1st character to last
# x = greeting_welcome[-5:]
# print(x)

## Strip - remove spaces

# remove_white_space = "remove spaces at end of string "
# print(len(remove_white_space))
# print(remove_white_space.strip()) # Removes spaces at end of string
# print(len(remove_white_space.strip())) # Length can bee seen to go down

## Data types

## Boolean

# use_text = "here's SOME text with lot's of text"
# print(use_text.count("text")) # Count function. Fins
# print(use_text.lower()) # Makes everything lower case
# print(use_text.upper()) # Makes everthing upper case
# print(use_text.capitalize()) # Makes frist letter capital
# print(use_text.replace("with", ",")) # Replaces with, with ,.
# for x in use_text:
#     if x.isupper() == 0:
#         use_text.replace(x, x.upper())
#
# print(use_text)

## List. Sames as arrays, store data.

# cheese_types = ['Brie', 'Cheddar', 'Gouda'] # square brackets indicate list
# cheese_types.append("Leicester Red") # Adds item to end of list
# cheese_types[1] = "Aged Cheddar" # Replaces item with indexing
# # cheese_types.remove('Brie')
# cheese_types.insert(3, "Dairy bell")
# print(cheese_types) # Display cheese_types means print!!!
# print(type(cheese_types)) # Prints out what the object is
# print(cheese_types[2:]) # Prints out item 3 onwards
# cheese_types.pop() # Gets rid of last item from list

# mix_type_string = [1, 2, 3], ["String1", "String2"]]
# int_list = [1, 2]
# str_list = ["String1", "String2"]
# new_list = str_list + int_list
# print(new_list)  # Lists can hold multiple data types
# complex_list = [[1,2,3], ["Hi", "Hiya"]]
# print(complex_list[1])

## Tuples, can use things that never change, NHSid etc.

# meats = ("Salami", "Chorizo", "Steak")
# print(meats)
#
# x = list(meats)
# x.insert(0, "Max")
# meats = tuple(x)
# print(meats)
#
# # y = ', '.join(meats)
# # print(y)

## Dictionary

# student_records = {
#     "Name": "Sam"  # Name is key, sam is value
#     , "Stream": "DevOps"
#     , "Topics_covered": 5
#     , "Completed_lessons": ["Tuples", "Lists", "Variables"]
# }  # Can have a list in a tuple

# student_records["Name"] = "Jeff"

# print(student_records["Completed_lessons"][2]) # fetching index of list in dictionary
# print(student_records["Name"]) # Fetching the value of name
# print(sorted(student_records)) # Sorts according to keys
# print(student_records.keys())  # Gets keys of dictionary
# print(student_records.values())  # Gets values of dictionaries
# print(student_records["Name"])  # Gets value from key in dictionary
# print(student_records.get("Name"))  # Different method of same thing

## adding two items to completed lessons then displaying it
# student_records["Completed_lessons"].append("Lists")
# student_records["Completed_lessons"].append("Built in methods")
# print(student_records["Completed_lessons"])  # Checking work

## Sets - basically unordered lists

# sports = {"Tennis", "Football", "Rugby"} # Creating a set
# sports.add("Cricket") # Adding item to set
# sports.discard("Tennis")  # Removing item from set
# print(sports)
#
# x = frozenset([1, 2, 3, 4])# Frozen set, rarely used.
# print(type(x))

## Control flow

# weather = "sunny"
# conditional_weather = "clear"

## using and operator and if loop
# if weather == "sunny" and conditional_weather != "rainy": # Both must be true, due to and
#     print("Beach time")
# elif weather == "snow":
#     print("Sad time")
# else:
#     print("Better luck next time")

## using or operator and if loop
# if weather == "sunny" or conditional_weather == "clear": # Both must be true, due to and
#     print("Beach time")
# elif weather == "snow":
#     print("Sad time")
# else:
#     print("Better luck next time")


## For loops

# list_data = [1, 2, 3, 4, 5]
# for item in list_data:
#     if item > 4:
#         break # Does not print 5 as it does not match item condition, so code stops
#     elif item < 2:
#         print(item, "Cool")
#     else:
#         print(item)

# word = "Lexicon"
# for ch in word:
#     print(ch.upper())

## Printing in single line
# word = "Lexicon"
# new_word = ""
#
# for x in word:
#     new_word += " " + x
#     if word[-1] == x:
#         print(new_word)

## Iterating through dictionary

# student_records = {
#     "Name": "Sam"  # Name is key, sam is value
#     , "Stream": "DevOps"
#     , "Topics_covered": 5
#     , "Completed_lessons": ["Tuples", "Lists", "Variables"]
# }
#
# for item in student_records:
#     print(student_records[item])

## While loop

# x = 0
#
# while x < 5: # While variable name with condition
#     print(f"this is a repeating message, message {x}") # Formatting allows placeholder
#     if x == 4: # If loop optional in while loop.
#         break
#     x += 1

### Exercises

## Exercise with movie age limits

# age = int(input("What is your age? \t"))
#
# if age > 21:
#     print(f"You can go to Las Vegas, you are {age}")
# elif age >= 18 < 21:
#     print("You can watch anything")
# elif 15 <= age < 18:
#     print("You cannot watch 18+ films")
# elif 12 < age < 15:
#     print("You cannot watch 15+ or 18+ films")
# elif age < 1:
#     print("Enter a valid age please")
# else:
#     print("PG films only for you, I'm afraid")

## Exercise with dictionary iteration

student_records = {
    "Name": "Brian"
    , "Location": "Manchester"
    , "Grade": 2
    , "Skills": ["Agile trained", "Teamwork", "Organised"]
}

for x in student_records:
    print(x, ':', (student_records[x]))

# Or

# for keys in student_records:
#     print(keys, ":", student_records.get(keys))