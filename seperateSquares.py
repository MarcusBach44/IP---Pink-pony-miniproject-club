import numpy as np
import cv2

img = cv2.imread("./Cropped and perspective corrected boards/2.jpg")

squarePieces = []
rows = [1, 2, 3, 4, 5]
squares = [1, 2, 3, 4, 5]
startHeightPos = 0
rowDivision = 0

height, width, channels = img.shape
fifthHeight: int = height // 5
fifthWidth: int = width // 5

def showSquare():
    squareDivision = 0
    #counter = 0
    for square in squares:
        squareDivision = squareDivision + fifthWidth
        squareSection = img[rowDivision - fifthHeight:rowDivision, squareDivision - fifthWidth:squareDivision]
        #cv2.imshow("img", squareSection)
        #cv2.waitKey(0)
        #counter = counter + 1
        square += square

for row in rows:
    rowDivision = rowDivision + fifthHeight
    showSquare()
    row += row

"""Use this for calling a square:

cv2.imshow("img", squarePieces[square_number])
cv2.waitKey(0)

The amount of squares is 0-24 and is counted left to right.
"""