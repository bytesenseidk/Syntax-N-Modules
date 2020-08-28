import os
from PIL import Image

def image_pdf(image_path):
    # Gets the last part of the path given, I.E. picture.png
    file_name = str(image_path.split("\\")[-1])

    # Replaces the image format extension to pdf
    new_file = os.path.join(image_path.replace(file_name.split(".")[-1], "pdf"))
    
    # Pillow instance of desired picture
    image_file = Image.open(image_path)
    parsed = image_file.convert("RGB")
    return parsed.save(new_file)

if __name__ == "__main__":
    image_path = input(r"Drag picture here >> ")
    image_pdf(image_path)

