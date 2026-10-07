import numpy as np
import cv2

img = cv2.imread("./Game pieces/Plain.png")

imgBlurred = cv2.medianBlur(img, 97)
#cv2.imshow("Blurred", imgBlurred)
#cv2.waitKey(0)

avrColorByRow = np.average(imgBlurred, axis=0)
avrColor = np.average(avrColorByRow, axis=0)

#Keep in mind at den printer det som BGR, fordi selvfølgelig gør den det  ._.
print(avrColor)
