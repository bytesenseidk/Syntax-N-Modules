class Factorial(object):
    def __init__(self, num):
        self.value = 1
        # Multiplies each number in num range with __mul__ method
        for i in range(1, num + 1):
            self *= i
        
    def __mul__(self, other):
        # Returns a new instance of the Factorial class with updated values
        self.value *= other
        return self
    
    def __repr__(self):
        # Provices a string representation of the object
        return str(self.value)
    
if __name__ == "__main__":
    factorial = Factorial(5)
    print(f"Factorial of 5: {factorial}")

    