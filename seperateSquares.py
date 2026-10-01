import numpy as np
import cv2

img = cv2.imread("./Cropped and perspective corrected boards/1.jpg")

rows = [1, 2, 3, 4, 5]
squares = [1, 2, 3, 4, 5]
startHeightPos = 0
rowDivision = 0

height, width, channels = img.shape
fifthHeight: int = height // 5
fifthWidth: int = width // 5

def showSquare():
    squareDivision = 0
    for square in squares:
        squareDivision = squareDivision + fifthWidth
        squareSection = img[rowDivision - fifthHeight:rowDivision, squareDivision - fifthWidth:squareDivision]
        cv2.imshow("img", squareSection)
        cv2.waitKey(0)
        square += square

for row in rows:
    rowDivision = rowDivision + fifthHeight
    showSquare()
    row += row