import os
import io
import pyqrcode
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

class BarCode(object):
    def __init__(self, data):
        if len(data) == 12 and data.isdigit():
            self.data = str(data)
        else:
            self.data = "123456789012"
        
    def generate(self):
        temp = io.BytesIO()
        EAN13(self.data, writer=ImageWriter()).write(temp)
        image = Image.open(temp).resize((400,400), Image.ANTIALIAS)
        image.show()

class QrCode(object):
    def __init__(self, data):
        self.data = data
    
    def generate(self):
        pyqrcode.create(self.data).png("temp.png", scale=10)
        image = Image.open("temp.png").resize((400,400), Image.ANTIALIAS)
        image.show()
        if os.path.exists("temp.png"):
            os.remove("temp.png")
    
if __name__ == "__main__":
    BarCode("123456789012").generate()
    QrCode("123456789012").generate()
    
