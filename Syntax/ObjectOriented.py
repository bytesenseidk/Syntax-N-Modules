class Dog(object):   # Parrent Class.
    race = "Pitbull" # Class Attribute.
    def __init__(self, name): # Constructor / Instantiator.
        """ Variables inside this is called instance attributes """
        self.name = name

    def __str__(self): # Magic / Special Method.
        """ String representation of the class """
        return str(f"Name: {self.name}\n"
                   f"Race: {Dog.race}\n"
                   f"{self.sit()}\n"
                   f"{self.bark()}")

    def sit(self): # Class Method.
        return str(self.name + " is sitting.")
    
    def bark(self):
        return str(self.name + " is barking!! ")

""" Inheritance """
class Puppy(Dog): # Child Class.
    def __init__(self, name):
        """ Constructor based on parrent class """
        super().__init__(name) # Inherit constructor from parrent.

    
    def bark(self): # Polymorphism
        """ Polymorphism makes you able to customize a inherrited method """
        return str(self.name + " can't bark!.")


if __name__ == "__main__":    # This runs our code, if we execute the script directly.
    snoopy = Dog("Snoopy")    # Instance of the Dog class.
    sniffy = Puppy("Sniffy")  # Instance of the Puppy class.
    print(snoopy)
    print(f"\n{'-' * 10}\n")
    print(sniffy)

