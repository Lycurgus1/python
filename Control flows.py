# Control flow

weather = "sunny"
conditional_weather = "clear"

# Using and operator and if loop
if weather == "sunny" and conditional_weather != "rainy": # Both must be true, due to and
    print("Beach time")
elif weather == "snow":
    print("Sad time")
else:
    print("Better luck next time")

# Using or operator and if loop
if weather == "sunny" or conditional_weather == "clear": # Both must be true, due to and
    print("Beach time")
elif weather == "snow":
    print("Sad time")
else:
    print("Better luck next time")

