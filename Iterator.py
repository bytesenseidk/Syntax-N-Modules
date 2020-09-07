
# Standard library - iter() module demo.
iterator = iter("abc")  # Results:
print(next(iterator))   #    a
print(next(iterator))   #    b
print(next(iterator))   #    c

# Pure Object-Oriented Iterator.
class Iterator(object):
    def __init__(self, step):
        self.step = step
    
    def __next__(self):
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step
    
    def __iter__(self):
        return self

if __name__ == "__main__":
    iteration = Iterator(5)
    [print(value) for value in iteration]

