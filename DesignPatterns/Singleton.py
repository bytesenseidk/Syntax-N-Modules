import sqlite3

""" Singleton Design Pattern:
Restricts the instantiation of a class to one 'single' instance.
Example: We have a database, and want to ensure only a single instance is making changes at a time,
this ensures that the data doesn't get currupted by multiple instances changing the value simultaneously.
"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class TrueDesignPattern(metaclass=Singleton):
    connection = None
    def __init__(self):
        self.cursor, self.connection = self.connect()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS TableName (time TEXT, day INT, comment TEXT)")

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("Database.db")
            self.cursor = self.connection.cursor()
        return self.connection, self.cursor

class FalseDesignPattern(object):
    connection = None
    def __init__(self):
        self.cursor, self.connection = self.connect()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS TableName (time TEXT, day INT, comment TEXT)")

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("Database.db")
            self.cursor = self.connection.cursor()
        return self.connection, self.cursor

if __name__ == "__main__":
    false_instance_0 = FalseDesignPattern()
    false_instance_1 = FalseDesignPattern()
    true_instance_0 = TrueDesignPattern()
    true_instance_1 = TrueDesignPattern()
    print(f"Without Singleton: is {False if false_instance_0 == false_instance_1 else True}\n",
         f"With Singleton:    is {True if true_instance_0 == true_instance_1 else False}\n")

