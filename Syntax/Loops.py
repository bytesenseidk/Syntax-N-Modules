def for_loop():
    # A for loop is used for iterating over a sequence 
    # (that is either a list, a tuple, a dictionary, a set, or a string).
    for i in "python_genius":
        print(i, end="")
    print("")

def while_loop():
    # The while loop in Python is used to iterate over a block of code 
    # as long as the test expression (condition) is true.
    while True:
        print("This will only execute a single time!")
        break # This stops the iteration and exits the for loop.

def continue_example():
    for letter in "Python":
        if letter == "h":
            continue # Skips the iteration if the letter "h" is reached.
        elif letter == "n":
            break # Breaks the loop when it reaches "n".
        print(letter, end="")

def list_comprehension():
    # List comprehension provides a way to create a loop in a single line.
    # This will always return a list though.
    print("")
    [print(i, end="") for i in "python_genius"]


if __name__ == "__main__":
    for_loop()
    while_loop()
    continue_example()
    list_comprehension()

