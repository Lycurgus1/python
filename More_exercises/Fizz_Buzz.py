# Creating class
class Fizz_Buzz:

    # Method, self not needed
    def fizz_buzz():
        # Counting through all numbers 1 to 100
        for number in range(100):
            # Conditional if number is worthy of Fizzbzz of fizz
            if (number % 3) == 0:
                if (number % 5) == 0:
                    print("FizzBuzz")
                else:
                    print("Fizz")
            # Conditional for if number is just for buzz
            elif (number % 5) == 0:
                print("Buzz")
            else:
                print(number)

# Testing
Fizz_Buzz.fizz_buzz()