import os
import time
from tqdm import tqdm
from pyfiglet import Figlet


def loading():
    for _ in tqdm(range(100), desc="Loading...", ascii=False, ncols=75):
        time.sleep(0.01)
    print("Loading Done!")

def font(text):
    # Instance of Figlet with font settings
    cool_text = Figlet(font="slant")
    return str(cool_text.renderText(text))

def window_size(columns=750, height=30):
    # Clear terminal window
    os.system("cls")
    # Set terminal window to a fixed size
    os.system(f'mode con: cols={columns} lines={height}')    

if __name__ == "__main__":
    window_size(80, 20)
    print(font("Python_Genius"))
    loading()


