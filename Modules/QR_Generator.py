import os
import pyqrcode
from PIL import Image

class QR_Gen(object):
    def __init__(self, text):
        self.qr_image = self.qr_generator(text)

    @staticmethod
    def qr_generator(text):
        pyqrcode.create(text).png("temp.png", scale=10)
        image = Image.open("temp.png").resize((400,400),Image.ANTIALIAS)
        image.show()
        if os.path.exists("temp.png"):
            os.remove("temp.png")

if __name__ == "__main__":
    QR_Gen(input("[QR] Enter text or link: "))
