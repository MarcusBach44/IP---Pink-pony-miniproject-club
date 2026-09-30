import numpy as np
import cv2

img = cv2.imread("./Game pieces/Water.png")
imgBlurred = cv2.medianBlur(img, 97)

avrColorByRow = np.average(imgBlurred, axis=0)
avrColor = np.average(avrColorByRow, axis=0)
#Keep in mind at den printer det som BGR, fordi selvfølgelig
print(avrColor)

"""#Here is where we should put the generalised colors of the squares - i just chose red, green and blue as a start
red = np.array([255, 0, 0])
green = np.array([0, 255, 0])
blue = np.array([0, 0, 255])

#Here are the square types
forestSquare = []
waterSquare = []
fieldSquare = []
mineSquare = []
hillSquare = []
desertSquare = []

def squareColor():
    return np.array([red, green, blue])

def square():
    if squareColor():
        return"""