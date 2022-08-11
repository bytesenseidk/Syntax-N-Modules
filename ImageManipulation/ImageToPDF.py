import os
from PIL import Image


class ImageToPDF(object):
    def __init__(self, image_path):
        self.image_path = image_path
        # Gets the last part of the path given, I.E. picture.png
        self.file_name = str(image_path.split("\\")[-1])
    
    def convert(self):
        try:
            # Replaces the image format extension to pdf
            new_file = os.path.join(self.image_path.replace(self.file_name.split(".")[-1], "pdf"))
            # Pillow instance of desired picture
            image_file = Image.open(self.image_path)
            result = image_file.convert("RGB")
            result.save(new_file)
            print("Convertion Successful..")
        except:   
            print("Convertion Unsuccessful..")


if __name__ == "__main__":
    image = input(r"Drag picture here >> ")
    ImageToPDF(image).convert()
    
