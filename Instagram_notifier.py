import requests
from win10toast import ToastNotifier

class Instagram_updater(object):
    def __init__(self, username):
        self.username = username
        self.current = ""
        self.last = ""

    def followers(self):
        url = 'https://www.instagram.com/' + self.username
        r = requests.get(url).text
        start = '"edge_followed_by":{"count":'
        end = '},"followed_by_viewer"'
        self.last = self.current
        self.current = str(r[r.find(start)+len(start):r.rfind(end)])
    
    def main(self, notification_rate):
        parser = ToastNotifier()
        while True:
            self.followers()
            message = f"Current Follows: {self.current}\nLast Check: {self.last}"
            parser.show_toast(self.username, message, duration=notification_rate)
    
if __name__ == "__main__":
    username = input(r"Enter Instagram username >> ")
    try:
        notify_rate = int(input("How often would you be notified in minutes?: >> ")) * 60
    except:
        notify_rate = 5 * 60
    account = Instagram_updater(username)
    account.main(notify_rate)


