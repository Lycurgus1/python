# Class variable 02/07/2020

class Dog:
    animal_kind = "canine" # Class variable - dangerous as can be overwritten outside the class

    def bark(self):
        self.animal_kind # Method variable inside the class, can only be overwritten inside the method
        return "woof"

jeff = Dog() # Instantuating our class/ creating an object

print(jeff.animal_kind)
print(jeff.bark())

jeff.animal_kind = "fish"
print(jeff.animal_kind)