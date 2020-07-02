# List. Sames as arrays, store data.

cheese_types = ['Brie', 'Cheddar', 'Gouda'] # square brackets indicate list
cheese_types.append("Leicester Red") # Adds item to end of list
cheese_types[1] = "Aged Cheddar" # Replaces item with indexing
# cheese_types.remove('Brie')
cheese_types.insert(3, "Dairy bell")
print(cheese_types) # Display cheese_types means print!!!
print(type(cheese_types)) # Prints out what the object is
print(cheese_types[2:]) # Prints out item 3 onwards
cheese_types.pop() # Gets rid of last item from list

mix_type_string = [1, 2, 3], ["String1", "String2"]]
int_list = [1, 2]
str_list = ["String1", "String2"]
new_list = str_list + int_list
print(new_list)  # Lists can hold multiple data types
complex_list = [[1,2,3], ["Hi", "Hiya"]]
print(complex_list[1])
