try:
    """ This will run first, if any errors occur, it skips to the except statement """
    print(hello)

except Exception as E:
    """ This will run if the try statement fails, which it will in this case """
    print(E) # This will print the exception our try statement returns
    print("hello is not defined..")

finally:
    """ This statement will always execute """
    print("Follow python_genius on Instagram!")

