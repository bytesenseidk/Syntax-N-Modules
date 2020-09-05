""" Todo: 
add threads
"""
import os
import time
import requests
from win10toast import ToastNotifier
from time import strftime

class Instagram_updater(object):
    def __init__(self, username):
        self.username = username
        self.current = "None"
        self.raise_count = 0
        self.first = "None"
        

    def followers(self):
        url = 'https://www.instagram.com/' + self.username
        r = requests.get(url).text
        start = '"edge_followed_by":{"count":'
        end = '},"followed_by_viewer"'
        self.current = str(r[r.find(start)+len(start):r.rfind(end)])
        try:
            if int(self.current) - int(self.first) > self.raise_count:
                self.raise_count = int(self.current) - int(self.first)
            elif int(self.current) - int(self.first) < self.raise_count:
                self.raise_count = int(self.current) - int(self.first)
            else:
                pass
        except:
            pass
        
    def main(self, notification_rate):
        parser = ToastNotifier()
        start_time = strftime("%H:%M:%S", time.localtime())
        self.followers()
        self.first = self.current
        # will catch type error the first and second iteration
        while True:
            try:
                data = str(f"Current Check:\t{int(self.current):,} Followers.\n"
                           f"Raise Count:\t{int(self.raise_count):,} Followers.\n"
                           f"Script Executed :\t{start_time}\n"
                           f"Start Amount:\t{int(self.first):,} Followers.")
                parser.show_toast(self.username, data, icon_path="logo.ico", 
                                                duration=notification_rate)
                self.followers()
            except:
                data = str(f"Current Check:\t{int(self.current):,} Followers.\n"
                           f"Raise Count:\t{self.raise_count} Followers.\n"
                           f"Script Executed:\t{start_time}\n"
                           f"Start Amount:\t{int(self.first):,} Followers.")
                parser.show_toast(self.username, data, icon_path="logo.ico", 
                                            duration=notification_rate)
                self.followers()


if __name__ == "__main__":
    os.system("cls")
    print(str("       [ InstaFy ]\n"
        "| Keep Track of Followers |\n\n"
        f'Script Started: {strftime("%H:%M:%S", time.localtime())}\n'
        "To Exit: [CTRL] + [C]\n\n"
        "Leave this window open...\n"))
    username = input(r"Enter Instagram username  >> ")
    try:
        notify_rate = int(input("Minutes between nofifications  >> ")) * 60
    except:
        notify_rate = 5 * 60
    account = Instagram_updater(username)
    account.main(notify_rate)

