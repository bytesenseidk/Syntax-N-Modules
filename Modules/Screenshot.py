import os
import pyautogui


def screenshot():
    # Save screenshot to picture folder inside your home folder
    save_path = os.path.join(os.path.expanduser("~"), "Pictures")
    shot = pyautogui.screenshot()
    # Save screenshot in set save_path
    shot.save(f"{save_path}\\python_screenshot.png")
    return print(f"\nScreenshot taken, and saved to {save_path}")


if __name__ == "__main__":
    screenshot()

