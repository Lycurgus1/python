# Default values in functions
def my_function(country = "Friesland"):
    if country in ("Denmark"):
        print("{} is a garbage country for garbage people".format(country))
    else:
        print("I am from", country)

my_function("Denmark")
my_function()