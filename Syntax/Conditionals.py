def standard_conditional(number):
    # The if-elif-else statement is used to execute both 
    # the true part and the false part of a given condition. 
    if number < 0:
        return "Negative number!"
    elif number == 0:
        return "Neutral number!"
    else:
        return "Positive number!"

def ternary_conditional(number):
    # Ternary operators let you test multiple conditions on a single line.
    if number < 0 and number > 0 or number == 0:
        return "The number is 0"
    else:
        return "The number is not 0"

def string_conditional(string):
    # String conditionals is used when you want to check if a string contains something or not.
    if "n" in string:
        return "String contains an 'n'"
    elif "n" not in string:
        return "String does not contain an 'n'"
    else:
        # Pass is used when the interpreter should ignore the statement or function.
        pass

if __name__ == "__main__":
    print(f"Standard Conditional: {standard_conditional(7)}")
    print(f"Ternary Conditional:  {ternary_conditional(7)}")
    print(f"String Conditional:   {string_conditional('Hello')}")
