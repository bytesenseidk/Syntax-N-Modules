import os
import instaloader

def download(username):
    instance = instaloader.Instaloader()
    os.chdir(os.path.join(os.path.expanduser("~"), "Desktop"))
    return instance.download_profile(username, profile_pic_only=True)

if __name__ == "__main__":
    download("python_genius")

