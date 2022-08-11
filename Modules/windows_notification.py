import os
from win10toast import ToastNotifier

def notification():
    # Change dir to the scripts location
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    toast = ToastNotifier() # Instance of ToastNotifier module
    title = "Notification"  # Title for message displayed
    message = "Follow python_genius on Instagram!"
    # Place image in the same dir as script
    icon = "icon.ico"
    length = 30
    toast.show_toast(title, message, icon_path=icon, duration=length)

notification()
