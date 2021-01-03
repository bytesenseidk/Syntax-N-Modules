string = "python_genius IS Awesome!"

cap = string.capitalize() # Capitalize the string.
low = string.lower() # Lowercase the string.
up = string.upper() # Uppercase the string.
swap = string.swapcase() # Swap cases in the string.
tit = string.title() # Titlecase the string.

if __name__ == "__main__":
    print(f"Origional String:   {string}")
    print(f"Capitalized String: {cap}")
    print(f"Lowercased String:  {low}")
    print(f"Uppercased String:  {up}")
    print(f"Swapcase String:    {swap}")
    print(f"Titlecase String:   {tit}")




# # String operations
# is_in = "python" in string
# not_in = "python" in string
# concat = string + "!!!"
# length = len(string)
# minimum = min(string)
# maximum = max(string)
# multi = string * 2
# index = string[6]
# slice = string[0:13]
# count = string.count("e")

# results = [cap,low,swap,tit,up,is_in,not_in,concat,length,minimum,maximum,multi,index,slice,count]
# for var in results:
#     print(var)