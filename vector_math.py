import math

""" Mathematics with vectors """
vector_1 = [7,9,4,3]
vector_2 = [9,8,7,6]

def addition(vector_1, vector_2):
    result = []
    for index, num in enumerate(vector_1):
        result.append(num + vector_2[index])
    return result

def subtraction(vector_1, vector_2):
    result = []
    for index, num in enumerate(vector_1):
        result.append(num - vector_2[index])
    return result

def scalar_multiplication(vector, scalar):
    result = []
    for num in vector:
        result.append(scalar * num)
    return result

print(f"Addition:     {vector_1} + {vector_2} = {addition(vector_1, vector_2)}")
print(f"Subtraction:  {vector_1} - {vector_2} = {subtraction(vector_1, vector_2)}")
print(f"Scalar Multiplication: 2 * {vector_2} = {scalar_multiplication(vector_2, 2)}")
print("\n")



def magnitude(vector):
    """ Length of a vector, denoted as: ||v|| """
    vector_sum = 0
    for num in vector:
        vector_sum += pow(num, 2)
    return math.sqrt(vector_sum)

def inner_product(vector_1, vector_2):
    """ Transpose or dot product """
    total = 0
    for index, num in enumerate(vector_1):
        total += (num * vector_2[index])
    return total


print(f"Magnitude of {vector_1} = {magnitude(vector_1)}")
print(f"Inner Product of {vector_1} & {vector_2} = {inner_product(vector_1, vector_2)}")
print("\n")



def triangle_inequality(vector_1, vector_2):
    """the magnitude of the sum of vectors is always less than 
    or equal to the sum of the magnitudes of the vectors:
    ||v + u|| <= ||v|| + ||u|| 
    """
    vector_sum = addition(vector_1, vector_2)
    vector_1_mag = magnitude(vector_1)
    vector_2_mag = magnitude(vector_2)
    mag_of_sum = magnitude(vector_sum)    
    sum_of_mag = vector_1_mag + vector_2_mag
    return  mag_of_sum <= sum_of_mag

def angle(vector_1, vector_2):
    transpose = inner_product(vector_1, vector_2)
    mag_1 = magnitude(vector_1)
    mag_2 = magnitude(vector_2)
    mag = mag_1 * mag_2
    return math.degrees(math.acos(transpose / mag))


print(f"Triangle of Inequality: {vector_1} & {vector_2} = {triangle_inequality(vector_1, vector_2)}")
print(f"Angle of {vector_1} and {vector_2} = {angle(vector_1, vector_2)}")


