import os
import sys
import sqlite3


class MetaSingleton(type):
    """ Insures only a single connection to the database is available at the time. """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    connection = None
    def __init__(self):
        """ Changes directory to script_path, creates a connection to the database if it exists, if not, it creates a new database.
        Creates a single table inside your database file called 'Table_1' if it dosen't exists already """
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.cursor, self.connection = self.connect()
        
        self.table_name = "Table_1"
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} (column_1 TEXT, column_2 INT, column_3 REAL)")
        
        
    def connect(self):
        """ Makes sure to make a connection to the database, if no connection is active """
        if self.connection is None:
            self.connection = sqlite3.connect("Database_file.db")
            self.cursor = self.connection.cursor()
        return self.cursor, self.connection
    
    
    def insert_data(self):
        """ Inserts data into our table """
        column_1 = "First Column"
        column_2 = 45
        column_3 = 45.77
        self.cursor.execute(f"INSERT INTO {self.table_name} (column_1, column_2, column_3) VALUES(?,?,?)", (column_1, column_2, column_3))
        self.connection.commit()

        
    def read_data(self):
        """ Reads data from our table """
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor.fetchall():
            print(row)


if __name__ == "__main__":
    database = Database()
    database.insert_data()
    database.read_data()
    if sys.exit():
        database.cursor.close()
        database.connection.close()