# Dictionary

student_records = {
    "Name": "Sam"  # Name is key, sam is value
    , "Stream": "DevOps"
    , "Topics_covered": 5
    , "Completed_lessons": ["Tuples", "Lists", "Variables"]
}  # Can have a list in a tuple

student_records["Name"] = "Jeff"

print(student_records["Completed_lessons"][2]) # fetching index of list in dictionary
print(student_records["Name"]) # Fetching the value of name
print(sorted(student_records)) # Sorts according to keys
print(student_records.keys())  # Gets keys of dictionary
print(student_records.values())  # Gets values of dictionaries
print(student_records["Name"])  # Gets value from key in dictionary
print(student_records.get("Name"))  # Different method of same thing

# Adding two items to completed lessons then displaying it
student_records["Completed_lessons"].append("Lists")
student_records["Completed_lessons"].append("Built in methods")
print(student_records["Completed_lessons"])  # Checking work

# Removing items
student_records.pop("Topics covered") # Removes item associated with key
student_records.popitem() # Removes last item added to list
del student_records["Name"] # Removes item with specific key name

# Can also clear copy and nest dictionaries.