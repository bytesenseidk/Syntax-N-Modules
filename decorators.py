

def mydecorator(function):
    def _mydecorator(*args, **kwargs):
        # Do some stuff before the real 
        # function gets called...
        result = str(f"Result: {function(*args, **kwargs)}")
        # Do some stuff after...
        print("This will print before our function...")
        return result
    # Returns the sub-function
    return _mydecorator

@mydecorator
def addition(a, b):
    return a + b


print(addition(1, 2))

