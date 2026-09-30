import numpy as np
import cv2

img = cv2.imread("./Cropped and perspective corrected boards/1.jpg")
#imgGray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

startHeightPos = 0

height, width, channels = img.shape
fifthHeight: int = height // 5

onefifthHeight = startHeightPos+fifthHeight
twofifthHeight = onefifthHeight+fifthHeight
threefifthHeight = twofifthHeight+fifthHeight
fourfifthHeight = threefifthHeight+fifthHeight
fivefifthHeight = fourfifthHeight+fifthHeight

print(fivefifthHeight)



"""top_section = image[:half_height, :]
bottom_section = image[half_height:, :]

cv2.imshow("img", topLeft)
cv2.waitKey(0)"""

"""corners = cv2.goodFeaturesToTrack(imgGray, 50, 0.6, 20)
corners = np.int64(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)"""

"""cv2.imshow("img", img)
cv2.waitKey(0)"""