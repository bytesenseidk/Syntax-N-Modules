def empty_func():
    """ This function is defined, but wont do anything """
    pass

def returning_func():
    """ This function will return the string "Hello!" """
    return "Hello!"

def parameter_func(parameter, default_parameter="Hello"):
    """ This function takes 1 or 2 parameters, a default parameter will be used if 
    no other value is passed to it. We will return this as a "format-string" """
    return f"{default_parameter} {parameter}!"

def unpacking_func(*args, **kwargs):
    """ This function can take an unlimited amount of arguments, * is called splat, 
    and accepts any amount of parameters, **kwargs accept any amount of keyword arguments """
    return [ar for ar in args]

def yielding_func(iterable=[1, 2, 3, 4, 5]):
    """ This function takes in an iterable parameter and yields each element, a yield function is also called a generator object.
    This saves memory by yielding each element one by one using the iterator protocol, instead of creating a new list, 
    which it only uses to feed another constructor """
    for element in iterable:
        yield element
    
def recursive_func(start=5):
    """ This function calls itself recursively until a condition is met, this can limit the amount of code needed in a function. """
    if start == 0:
        return "Recursive function ended."
    return recursive_func(start-1)

def decorator_func(func):
    """ This function can """
    def inner_func(*args, **kwargs):
        print(len(args))
        return args
    return inner_func

@decorator_func
def decorated_func(a, b):
    return a + b

if __name__ == "__main__":
    """ The main function in python; this function only executes if this script is run directly """
    print(f"[ FUNCTION DEMONSTRATION ]\n",
            f"{empty_func()}\n",
            f"{returning_func()}\n",
            f"{parameter_func('Followers')}\n",
            f"{unpacking_func([1], [2], [3], [4], print, sum)}\n",
            f"{list(yielding_func())}\n",
            f"{recursive_func()}\n"
            f"{decorated_func(1, 2)}")
