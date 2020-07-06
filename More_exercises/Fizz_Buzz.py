class Fizz_Buzz:

    def fizz_buzz():
        for number in range(100):
            if (number % 3) == 0:
                if (number % 5) == 0:
                    print("FizzBuzz")
                else:
                    print("Fizz")
            elif (number % 5) == 0:
                print("Buzz")
            else:
                print(number)

Fizz_Buzz.fizz_buzz()