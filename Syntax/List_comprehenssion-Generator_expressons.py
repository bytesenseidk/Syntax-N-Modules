"""
List Comprehenssions; Used explicitly to create lists
"""

print(f'{"="*10} List Comprehenssions {"="*10}')
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
alpha_num = {"a", "b", "c", "d", "e", "f"}

comp_squared = [num*num for num in numbers]
comp_evens = [num for num in numbers if num % 2 == 0]
ascii_val = list(filter(lambda num: num, map(ord, alpha_num)))

print(f"List Comprehenssion: {comp_squared}\n"
      f"List Comprehenssion: {comp_evens}\n"
      f"List Comprehenssion: {ascii_val}\n")


def cartesian_product_example_1():
    colors = ["Black", "White"]
    sizes = ["S", "M", "L"]
    tshirts = [(color, size) for color in colors for size in sizes]
    for tshirt in tshirts:
        print(tshirt)
    print("\n")

cartesian_product_example_1()


def cartesian_product_example_2():
    colors = ["Black", "White"]
    sizes = ["S", "M", "L"]
    tshirts = [(color, size) for size in sizes 
                             for color in colors]
    print(tshirts, "\n")

cartesian_product_example_2()


"""
Generator Expressions - Saves memory by yielding elements one by one using the iterator protocol, 
instead of building a whole list just to feed another constructor.
"""

print(f'{"="*10} Generator Expressions {"="*10}')

numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
alpha_num = {"a", "b", "c", "d", "e", "f"}

genexp_squared = tuple(num * num for num in numbers)
genexp_evens = tuple(num for num in numbers if num % 2 == 0)

print(f"Generator Exp Squared:   {genexp_squared}\n"
      f"Generator Exp Evens:     {genexp_evens}\n")


sizes = {"S", "M", "L"}
colors = {"Black", "White"}

for tshirt in (f"Color: {color} | Size: {size}" for color in colors for size in sizes):
    print(tshirt)

