import io
from barcode import EAN13
from barcode.writer import ImageWriter
from PIL import Image

def bar_generator(digits=123456789123):
    # digits=123456789123 is a default value, if no other values is passed.
    # io.BytesIO makes sure you only save to memory instead of disk.
    rv = io.BytesIO()
    EAN13(str(digits), writer=ImageWriter()).write(rv)
    image = Image.open(rv)
    # Resize and display the BAR code
    image = image.resize((400,400), Image.ANTIALIAS)
    image.show()

if __name__ == "__main__":
    bar_generator()

