## Try, except loops
# Try, except, else, finally

def read_text_file(self):
    # Tries try statement. If works run else
    # Put code you think will raise exception
    try:
        file = open(self.file_path, "r")
    # Except runs if error occurs
    # If certain error occurs can do specific thing
    except NameError:
        print("Variable file is not defined")
    # Catches thrown exception
    except Exception as e:
        print(e)
    # Runs if try statement succeeds(if no exception)
    else:
        file.tell()
        self.text_storage = file.read(10)
        file.close()
        return self.text_storage
    # Will always run, irrelevant of exception
    # Mandatory code
    finally:
        print("this will always run")
# Tries to print x but its not defined
try:
    print(x)
# So throws error as except, in case or stopping program
except:
    print("An exception occured")

# # Raise an exception with if loop
# x = 6
#
# # If this is true, raise exception
# if x < 0:
#     raise Exception("No numbers below zero")
# else:
#     print(x)

# # Raising specific errors with if loop
# x = "test"
#
# # If loop with type specifiers
# if type(x) is not int: # If type(x) is str also possible
#     raise TypeError("Only strings allowed")

# # While loop + try, except means ensuring correct user input
# def raiseException():
#     while True:
#         try:
#             first_value = input("Enter name here\n")
#             if len(first_value) <= 0:
#                 raise Exception
#         except Exception:
#             print("We do not accept empty names")
#         else:
#             print("Thank you for entering your name")
#             return first_value
#
# raiseException()