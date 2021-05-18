import io
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image


class Bar_Gen(object):
    def __init__(self, digits):
        self.bar_image = self.bar_generator(digits)


    @staticmethod
    def bar_generator(digits):
        rv = io.BytesIO()
        EAN13(str(digits), writer=ImageWriter()).write(rv)
        image = Image.open(rv)
        image = image.resize((400,400), Image.ANTIALIAS)
        image.show()


if __name__ == "__main__":
    Bar_Gen(int(input("[BAR] Enter 12 digits: ")))
