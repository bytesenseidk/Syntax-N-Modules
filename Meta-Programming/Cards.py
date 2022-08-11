import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"]) # Constructs a simple class to represent individual cards.
# namedtuple can be used to build classes of objects that are just bundles of attrubutes with no custom methods,
# like a database record.

class DeckOfCards(object):
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")   # Using list comprehenssion to create each card
    suits = "spades diamonds clubs hearts".split()          # Splits string into an array of card suits

    def __init__(self):
        """ Initializes a deck of cards, using a list comprehenssion """
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    
    def __len__(self):
        """ Allows the len() call to work on the class. The len() function will attempt to call this 
        'dunder method' on the class """
        return len(self._cards)
    
    
    def __getitem__(self, position):
        """ Delegates to the [] operator of self._cards, making our deck automatically suports slicing """
        return self._cards[position]
    
    
    def get_random(self, card):
        """ Picks a random card from the initialized deck of cards. """
        return choice(self._cards)
    
    
    def __str__(self):
        """ Returns a string representation of the methods of this class. """
        deck_length = len(self._cards)
        random_card = self.get_random(self._cards)
        return str(f"Length:\t\t{deck_length}\nRandom Card:\t{random_card}")


if __name__ == "__main__":
    print(DeckOfCards())

