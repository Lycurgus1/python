# Create a calculator with a class. Should have methods to +, -, /, *, %
# Create class object
# Run class
class Python_Calulcator:

    def add_values(self, num1, num2): # Self key word refers to the class
        return num1 + num2

    def subtract_values(self, num1, num2):
        return num1 - num2

    def divide_values(self, num1, num2):
        return num1 / num2

    def multiply_values(self, num1, num2):
        return num1 * num2

    def remainder_values(self, num1, num2):
        return num1 % num2

print(Python_Calulcator.subtract_values("Jim", -1, 3))

object = Python_Calulcator()

print(object.add_values(1, 2))