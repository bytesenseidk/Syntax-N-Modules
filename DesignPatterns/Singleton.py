import sqlite3


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class FalseDesignPattern():
    connection = None
    def __init__(self):
        self.cursor, self.connection = self.connect()
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS TableName (time TEXT, day INT, comment TEXT)")

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("Database.db")
            self.cursor = self.connection.cursor()
        return self.connection, self.cursor


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


if __name__ == "__main__":
    false_instance_0 = FalseDesignPattern()
    false_instance_1 = FalseDesignPattern()
    true_instance_0 = TrueDesignPattern()
    true_instance_1 = TrueDesignPattern()
    print("- Singleton Design Pattern: Restricts the instantiation of a class to one 'single' instance.\n",
          "This is useful when exactly one object is needed to coordinate actions across the system.\n\n",
         f"Without Singleton: is {False if false_instance_0 == false_instance_1 else True}\n",
         f"With Singleton:    is {True if true_instance_0 == true_instance_1 else False}\n")

