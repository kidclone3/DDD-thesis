# Python script to crop images using OpenCV 

import cv2
import os

# Function to crop images

def crop_images(input_folder, image_name, x, y, w, h):
    img = cv2.imread(os.path.join(input_folder, image_name))
    crop_img = img[y:y+h, x:x+w, :]
    cv2.imwrite(os.path.join(input_folder, f"{image_name}"), crop_img)

if __name__ == '__main__':

    # Input folder path
    input_folder = './'

    # Crop coordinates
    x = 0
    y = 0

    # Width and height of the cropped image
    w = 341
    h = 290

    # Call the function
    crop_images(input_folder, "Figure5d.jpg", x, y, w, h)
