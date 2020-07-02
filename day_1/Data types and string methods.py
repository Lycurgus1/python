# Data types and string methods

use_text = "here's SOME text with lot's of text"
print(use_text.count("text")) # Count function. Fins
print(use_text.lower()) # Makes everything lower case
print(use_text.upper()) # Makes everthing upper case
print(use_text.capitalize()) # Makes frist letter capital
print(use_text.replace("with", ",")) # Replaces with, with ,.
for x in use_text:
    if x.isupper() == 0:
        use_text.replace(x, x.upper())

print(use_text)
