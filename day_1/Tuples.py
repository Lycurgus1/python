# Tuples, can use things that never change, NHSid etc.

meats = ("Salami", "Chorizo", "Steak")
print(meats)

x = list(meats)
x.insert(0, "Max")
meats = tuple(x)
print(meats)

# y = ', '.join(meats)
# print(y)
