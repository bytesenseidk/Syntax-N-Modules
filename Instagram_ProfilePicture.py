import os
import instaloader

def download(username):
    instance = instaloader.Instaloader()
    # Change working directory to the desktop
    os.chdir(os.path.join(os.path.expanduser("~"), "Desktop"))
    return instance.download_profile(username, profile_pic_only=True)

if __name__ == "__main__":
    print("Enter Username:")
    username = input(r"  >> ")
    download(username)

