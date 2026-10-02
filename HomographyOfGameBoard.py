import numpy as np
import cv2

#Laura brugte canny edge detection

"""grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayImg = cv2.bilateralFilter(grayImg, 1, 70, 70)
edges = cv2.Canny(grayImg, 50, 50)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

cv2.imshow("dede", closed)
cv2.waitKey(0)"""

# Load image in grayscale
img = cv2.imread("./manipulated pictures/RGB variance manipulation.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""# Apply Sobel operator
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Vertical edges

# Compute gradient magnitude
gradient_magnitude = cv2.magnitude(sobelx, sobely)

# Convert to uint8
gradient_magnitude = cv2.convertScaleAbs(gradient_magnitude)

dilated_img = cv2.dilate(gradient_magnitude, (7,7), iterations=15)

thresh = cv2.threshold(dilated_img, 80, 255, cv2.THRESH_BINARY)[1]"""

_, thresh = cv2.threshold(imgGray, 58, 255, cv2.THRESH_BINARY)
conturs, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contourImage = img.copy()
cv2.drawContours(contourImage, conturs, -1, (0, 0, 255), 3)


"""corners = cv2.goodFeaturesToTrack(imgGray, 160, 0.9, 7)
corners = np.int64(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 9, (0, 0, 255), -1)"""



# Display result
cv2.imshow("Sobel Edge Detection", img)

cv2.waitKey(0)
cv2.destroyAllWindows()



"""blurred = cv2.GaussianBlur(grayImg, (31, 31), 0)
thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("dede", thresh)
cv2.waitKey(0)"""

"""###I need the machine to do Homography
srcImg = cv2.imread("./Full game areas/DSC_1263.JPG")
# Four corners of the book in source image
srcCorners = np.array([[141, 131], [480, 159], [493, 630],[64, 601]])
# Read destination image.
destImg = cv2.imread("./Cropped and perspective corrected boards/1.jpg")
# Four corners of the book in destination image.
destCorners = np.array([[318, 256],[534, 372],[316, 670],[73, 473]])
# Calculate Homography
h, status = cv2.findHomography(srcCorners, destCorners)
# Warp source image to destination based on homography
imgOutput = cv2.warpPerspective(srcImg, h, (destImg.shape[1],destImg.shape[0]))

cv2.imshow("Source Image", srcImg)
cv2.imshow("Destination Image", destImg)
cv2.imshow("Warped Source Image", imgOutput)

cv2.waitKey(0)"""