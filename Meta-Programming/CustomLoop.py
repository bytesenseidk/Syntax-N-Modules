class CustomIterable(object):
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        # Makes the class iterable (Able to loop through)
        return CustomLoop(self.string)


class CustomLoop(object):
    def __init__(self, string):
        # Converts string to a list of words
        self.words = [word for word in string.split()]
        self.index = 0

    def __next__(self):
        # Will select the next item in the iterable for each call to the next method.
        if self.index == len(self.words):
            # Will stop the iteration when the list of words ends
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        # Returns a single word for each call.
        return word

    def __iter__(self):
        # Treats the class as an iterable itself, makes us able to loop through.
        return self


if __name__ == '__main__':
    iterable = CustomIterable("Want to learn Python? Follow python_genius today!")
    iterator =  iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

