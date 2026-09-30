import numpy as np
import cv2

img = cv2.imread("./Game pieces/Water.png")
imgBlurred = cv2.medianBlur(img, 97)

avrColorByRow = np.average(imgBlurred, axis=0)
avrColor = np.average(avrColorByRow, axis=0)

#Keep in mind at den printer det som BGR, fordi selvfølgelig gør den det  ._.
print(avrColor)
