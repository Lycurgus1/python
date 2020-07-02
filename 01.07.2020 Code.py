### Exercises

## Exercise with movie age limits

age = int(input("What is your age? \n"))

if age > 21:
    print(f"You can go to Las Vegas, you are {age}")
elif age >= 18 < 21:
    print("You can watch anything")
elif 15 <= age < 18:
    print("You cannot watch 18+ films")
elif 12 < age < 15:
    print("You cannot watch 15+ or 18+ films")
elif age < 1:
    print("Enter a valid age please")
else:
    print("PG films only for you, I'm afraid")

# ## Exercise with dictionary iteration
#
# student_records = {
#     "Name": "Brian"
#     , "Location": "Manchester"
#     , "Grade": 2
#     , "Skills": ["Agile trained", "Teamwork", "Organised"]
# }
#
# for x in student_records:
#     print(x, ':', (student_records[x]))

# Or

# for keys in student_records:
#     print(keys, ":", student_records.get(keys))