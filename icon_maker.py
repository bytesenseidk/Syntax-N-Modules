import os
import PIL.Image

class Icon_Maker(object):
    def __init__(self, picture_path):
        self.picture_path = picture_path.split("\\")
        self.picture = self.picture_path[-1]
        self.picture_ext = self.picture.split(".")[-1]
        os.chdir(os.path.join(picture_path.strip(self.picture)))

    def convertion(self, icon_size=[(32, 32)]):
        img = PIL.Image.open(self.picture)
        try:
            self.picture = self.picture.replace(self.picture_ext, "ico")
            img.save(self.picture, sizes=icon_size)
            print("Image converted!")
        except Exception:            
            print("Image not converted!\n", Exception)


if __name__ == '__main__':
    print("Drag and drop picture file here:")
    picture = input("  >> ")
    icon = Icon_Maker(picture)
    icon.convertion()