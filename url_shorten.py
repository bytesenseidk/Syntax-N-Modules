import pyshorteners

def shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

if __name__ == "__main__":
    url = input("Enter link to shorten: ")
    print(f"\n{shorten(url)}")

