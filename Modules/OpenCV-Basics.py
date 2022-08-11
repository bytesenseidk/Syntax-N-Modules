import os
import cv2
import random
import datetime

class ImageRotate(object):
    def __init__(self, image):
        # Load the image into OpenCV and converts it into a numpy array.
        self.image_name = image.split("/")[-1]
        self.image = cv2.imread(image, 1)
        # Timestamp for image_name
        self.timestamp = datetime.datetime.now().strftime("%d%m%H%M%S")
        # Creates a folder for manipulated pictures.
        if not os.path.exists("Results/"):
            os.mkdir("Results")

    def save_image(self):
        # Save the image to the Results folder.
        cv2.imwrite(f"Results/{self.image_name}_{self.timestamp}", self.image)

    def show_image(self):
        # Shows the image until a key is pressed.
        cv2.imshow("Manipulated Image", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def rotation(self):
        # Resize the image.
        self.image = cv2.resize(self.image, (0, 0), fx=.5, fy=.5)
        # Rotates the image.
        self.image = cv2.rotate(self.image, cv2.cv2.ROTATE_90_CLOCKWISE)
        self.show_image()

    def scramble(self):
        # Fills first 100 rows of the picture array with random colors
        for i in range(100):
            for j in range(self.image.shape[1]):
                # Color-code: Blue, Green, Red
                self.image[i][j] = [random.randrange(255),
                                    random.randrange(255),
                                    random.randrange(255)]
        self.show_image()

    def slice(self):
        # copies the pixels from row 500 to 700 and column 600 to 900
        cut = self.image[500:700, 600:900]
        # Replaces pixels with the copied pixels
        self.image[100:300, 650:950] = cut
        self.show_image()

if __name__ == "__main__":
    # img = input(r"Enter path to picture  >> ")
    img = "image.jpg"
    image = ImageRotate(img)
    image.slice()

