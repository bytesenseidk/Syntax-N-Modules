import PIL.Image


def icon_maker(image, size=(32, 32)):
    file_ext = image.split(".")[-1]
    img = PIL.Image.open(image)
    img.save(f"{image.strip(f'.{file_ext}')}.ico", sizes=size)
    print(f"{image} have been convertet into an icon!")


if __name__ == "__main__":
    print("Drag image here:\n")
    image = input(r"  >> ")
    icon_maker(image)
