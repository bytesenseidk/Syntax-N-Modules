def function(argument):
    # Basic function that takes a single argument, which can be anything you like.
    return argument

def gen_function(iterable):
    # Generator function takes an iterable, manipulates the data, and returns a new iterable.
    for element in iterable:
        yield element

def recu_function(num):
    # Recursive function returns itself until a certain value is reached.
    if num == 1:
        return num
    else:
        return num + recu_function(num-1)

# An anonymous or lambda function lets you create functions in one line, 
# lets you return it as a variable and much more! 
anon_function = lambda a, b: a + b

if __name__ == "__main__":
    # This is the pythonic version of the main function.
    # The main function is the first function that runs when a script is executed.
    print(f"Standard Function:   {function('python_genius')}")
    print(f"Generator Function:  {[*gen_function('python_genius')]}")
    print(f"Recursive Function:  {recu_function(5)}")
    print(f"Anonymous Function:  {anon_function(1, 2)}")


