import os
import sqlite3

class MetaSingleton(type):
    """ Ensures only a single database connection exists at a time. """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    """ Singleton Class to Manage SQLite3 Database Operations """
    connection = None

    def __init__(self):
        """ Initializes the database, ensures the 'Table_1' exists. """
        self.db_name = "Database_file.db"
        self.table_name = "Table_1"
        self._setup()

    def _setup(self):
        """ Setup database connection and table creation """
        os.chdir(os.path.dirname(os.path.realpath(__file__)))  # Ensure directory consistency
        self.connect()
        self.create_table()

    def connect(self):
        """ Establishes a single database connection """
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        return self.cursor

    def create_table(self):
        """ Creates 'Table_1' if it doesn't already exist """
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                column_1 TEXT,
                column_2 INTEGER,
                column_3 REAL
            )
        """)
        self.connection.commit()

    def insert_data(self, column_1="First Column", column_2=45, column_3=45.77):
        """ Inserts sample data into the table """
        self.cursor.execute(f"INSERT INTO {self.table_name} VALUES (?, ?, ?)", (column_1, column_2, column_3))
        self.connection.commit()

    def read_data(self):
        """ Reads and displays data from the table """
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def close(self):
        """ Closes the database connection """
        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":
    print("=== Without Singleton Pattern ===")
    conn1 = sqlite3.connect("Database_file.db")
    conn2 = sqlite3.connect("Database_file.db")

    print(f"Connection 1 ID: {id(conn1)}")
    print(f"Connection 2 ID: {id(conn2)}")
    print("\nResult: Two different connections are created.")

    conn1.close()
    conn2.close()

    print("\n=== Demonstrating Singleton Behavior ===")
    db1 = Database()
    db2 = Database()

    print(f"Database 1 Connection ID: {id(db1.connection)}")
    print(f"Database 2 Connection ID: {id(db2.connection)}")
    print("\nResult: Both instances share the same connection.")

    print("\n=== Demonstrating Database Operations ===")
    db1.insert_data()
    print("Data in the database:")
    db1.read_data()

    db1.close()
