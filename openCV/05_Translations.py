import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('Images/1.jpg')


#  Function to translate the image
def translate(image, x, y):
    # Define the translation matrix and perform the translation
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


# Function to rotate the image
def rotate(image, angle, center=None, scale=1.0):
    # Get the dimensions of the image
    (h, w) = image.shape[:2]

    # If the center is None, initialize it as the center of the image
    if center is None:
        center = (w / 2, h / 2)

    # Perform the rotation
    M = cv.getRotationMatrix2D(center, angle, scale)
    rotated = cv.warpAffine(image, M, (w, h))
    return rotated

    



cv.waitKey(0)