
import os
import time
import sqlite3
import datetime
import requests


class Follower_Database(object):
    def __init__(self, username):
        self.username = username
        self.connection = sqlite3.connect("Database_File.db")
        self.cursor = self.connection.cursor()
        self.followers = self.current_followers()
        self.current_date = str(datetime.datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y %H:%M:%S"))
    
    def current_followers(self):
        url = 'https://www.instagram.com/' + self.username
        r = requests.get(url).text
        start = '"edge_followed_by":{"count":'
        end = '},"followed_by_viewer"'
        return int(r[r.find(start)+len(start):r.rfind(end)])
    
    def save_data(self):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.username}(Followers INT, Date TEXT)")
        self.cursor.execute(f"INSERT INTO {self.username}(Followers, Date) VALUES(?,?)", 
                                                    (self.followers, self.current_date))
        self.connection.commit()
        print("Data Saved..")
    
    def read_data(self):
        self.cursor.execute(f"SELECT * FROM {self.username}")
        for followers, date in self.cursor.fetchall():
            print(f"Followers: {followers:,}\tDate: {date}")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    print("Enter Instagram Username")
    user = input(r"  >> ")
    database = Follower_Database(user)
    os.system("cls")
    while True:
        print("[ INSTAGRAM TRACKER ]\n"
           f"Logged in as: {database.username}\n"
           f"Current Followers: {database.followers:,}\n\n"
            "[0] Exit Program.\n"
            "[1] Save Data.\n"
            "[2] Read Data\n\n")
        try:
            menu = int(input("  >> "))
            if menu == 0:
                break
            elif menu == 1:
                database.save_data()
                break
            elif menu == 2:
                database.read_data()
                break
            else:
                continue
        except Exception:
            print(Exception())
            time.sleep(10)
            continue
    database.cursor.close()
    database.connection.close()

