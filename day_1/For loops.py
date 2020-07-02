# For loops

list_data = [1, 2, 3, 4, 5]
for item in list_data:
    if item > 4:
        break # Does not print 5 as it does not match item condition, so code stops
    elif item < 2:
        print(item, "Cool")
    else:
        print(item)

word = "Lexicon"
for ch in word:
    print(ch.upper())

# Printing in single line
word = "Lexicon"
new_word = ""

for x in word:
    new_word += " " + x
    if word[-1] == x:
        print(new_word)

# Iterating through dictionary

student_records = {
    "Name": "Sam"  # Name is key, sam is value
    , "Stream": "DevOps"
    , "Topics_covered": 5
    , "Completed_lessons": ["Tuples", "Lists", "Variables"]
}

for item in student_records:
    print(student_records[item])
