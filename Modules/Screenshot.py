import pyautogui
from os import chdir, path
# Change directory to your desktop
chdir(path.join(path.expanduser('~'), 'Desktop'))

# Create an instance for the screenshot 
# function in the pyautogui module
instance = pyautogui.screenshot()
instance.save("Screenshot.png")
print("Screenshot saved to the desktop!")


