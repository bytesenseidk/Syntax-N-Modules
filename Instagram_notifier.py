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
        self.last = "None"
        self.first = "None"
        

    def followers(self):
        url = 'https://www.instagram.com/' + self.username
        r = requests.get(url).text
        start = '"edge_followed_by":{"count":'
        end = '},"followed_by_viewer"'
        self.last = self.current
        self.current = str(r[r.find(start)+len(start):r.rfind(end)])
    
    
    def main(self, notification_rate):
        parser = ToastNotifier()
        start_time = strftime("%H:%M:%S", time.localtime())
        self.followers()
        self.first = self.current
        # will catch type error the first and second iteration
        while True:
            try:
                data = str(f"Current Amount:\t{int(self.current):,}\n"
                           f"Last Amount:\t{int(self.last):,}\n"
                           f"Time Started:\t{start_time}\n"
                           f"Started With:\t{int(self.first):,}")
                parser.show_toast(self.username, data, icon_path="logo.ico", 
                                                duration=notification_rate)
                self.followers()
            except:
                data = str(f"Current Amount:\t{int(self.current):,}\n"
                           f"Last Amount:\t{self.last}\n"
                           f"Time Started:\t{start_time}\n"
                           f"Started With:\t{int(self.first):,}")
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
