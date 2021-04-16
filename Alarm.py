import time
import winsound
from win10toast import ToastNotifier

class Alarm(object):
    def __init__(self, message="Default Message", minutes=60):
        self.message = message
        self.minutes = minutes
        self.notificator = ToastNotifier()

        
    def start(self):
        # Notification Details
        self.notificator.show_toast("Alarm",
            f"Alarm wil go off in {self.minutes} minutes..", 
            duration=50)
        # Pause Script
        time.sleep(self.minutes * 60)
        # Alarm Sound
        winsound.Beep(frequency=2500, duration=1000)
        # Show Notification
        self.notificator.show_toast(f"Alarm", self.message, duration=50)


if __name__ == "__main__":
    Alarm("Post on github!", 1).start()


