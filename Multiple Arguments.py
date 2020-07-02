# Multiple Arguments

def my_first_function(*args):
    # print(type(args))
    for arg in args:
        print("Wrong", arg)
    return args # Return ends the function
    # print("This function works,", args)

my_first_function("jim", "Harry")