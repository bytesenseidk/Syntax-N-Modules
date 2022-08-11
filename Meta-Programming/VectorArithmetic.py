import inspect
from math import hypot, sqrt

class VectorArithmetic(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        # Parameter count; self, x & y
        self.p_count = len(inspect.signature(VectorArithmetic.__init__).parameters.values()) - 1

    def __repr__(self):
        # Representation of the Vector class.
        return f"Vector{self.x, self.y}"

    def __abs__(self):
        # Magnitude/Length of the vector ||v||
        return round(hypot(self.x, self.y), 2)

    def __add__(self, other):
        # Addition of vectors(Add 2 objects together).
        x = self.x + other.x
        y = self.y + other.y
        return VectorArithmetic(x, y)

    def __sub__(self, other):
        # Subtraction of vectors.
        x = self.x - other.x
        y = self.y - other.y
        return VectorArithmetic(x, y)

    def __mul__(self, scalar=1):
        # Scalar multiplication(Multiply each value in the vector by a scalar).
        return VectorArithmetic(self.x * scalar, self.y * scalar)

    def __call__(self):
        # Describes the instance of the class if called directly.
        print(f"Vector Instance: {VectorArithmetic(self.x, self.y)}")

    def triangle_inequality(self, other):
        # The magnitude of the sum of vectors is always less than or equal to the
        # sum of the magnitudes of the vectors: ||v + u|| <= ||v|| + ||u||
        vector_0, vector_1 = VectorArithmetic(self.x, self.y), VectorArithmetic(other.x, other.y)
        vector_0_mag, vector_1_mag = vector_0.__abs__(), vector_1.__abs__()
        mag_of_sum = vector_0.__add__(vector_1).__abs__()
        return  mag_of_sum <= vector_0_mag + vector_1_mag

    def arithmetic_mean(self):
        # Sum of values divided by the amount of values.
        return abs((self.x + self.y) / self.p_count)

    def geometric_mean(self):
        # Sum of values multiplied together, then take a square root
        # (for two numbers), cube root (for three numbers) etc.
        return round(sqrt(self.x * self.y), 2)

if __name__ == "__main__":
    vector_0 = VectorArithmetic(7, 10)
    vector_1 = VectorArithmetic(3, 7)
    methods = {
        "added": vector_0.__add__(vector_1),
        "subtracted": vector_0.__sub__(vector_1),
        "scaled": vector_0.__mul__(5),
        "magnitude": vector_0.__abs__(),
        "arit_mean": vector_0.arithmetic_mean(),
        "geo_mean": vector_0.geometric_mean(),
        "inequality": vector_0.triangle_inequality(vector_1)
    }
    for key in methods:
        print(key, ": \t", str(methods[key]))

