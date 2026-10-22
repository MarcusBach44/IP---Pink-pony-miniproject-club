import numpy as np
import cv2
from networkx.algorithms import hierarchy
import imutils

"""
img = cv2.imread("./Full game areas/Single Board Area/OneBoard1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thres = 28

blur = cv2.GaussianBlur(gray, (29, 29), 2)
edges = cv2.Canny(blur, thres, thres)

gray = np.float32(edges)
dst = cv2.cornerHarris(edges, 10, 27, 0.06)

# result is dilated for marking the corners, not important
dst = cv2.dilate(dst, None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.04 * dst.max()] = [0, 0, 255]

cv2.imshow("dede", img)
cv2.waitKey(0)"""

#######################################

"""img = cv2.imread("./Full game areas/Single Board Area/OneBoard1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thres = 28

blur = cv2.GaussianBlur(gray, (29, 29), 2)
edges = cv2.Canny(blur, thres, thres)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
drawing = np.zeros((edges.shape[0], edges.shape[1], 3), dtype=np.uint8)
for i in range(len(contours)):
    cv2.drawContours(drawing, contours, i, (0,0,255), 2, cv2.LINE_8, hierarchy, 3)


cv2.imshow("dede", edges)
cv2.waitKey(0)"""

#######################################

"""thres = 28

blur = cv2.GaussianBlur(gray, (29, 29), 2)
edges = cv2.Canny(blur, thres, thres)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Approximate contours to polygons + get bounding rects and circles
contours_poly = [None]*len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(c, 3, True)

drawing = np.zeros((edges.shape[0], edges.shape[1], 3), dtype=np.uint8)

# Draw polygonal contour + bonding rects + circles
for i in range(len(contours)):
    color = (0, 0, 255)
    cv2.drawContours(drawing, contours_poly, i, color)

cv2.imshow("dede", drawing)
cv2.waitKey(0)"""

####################################
"""
blur = cv2.GaussianBlur(gray, (41, 41), 5)
edges = cv2.Canny(blur, 28, 28)

ret, thresh = cv2.threshold(edges, 3, 55, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(img.copy(), contours, -1, (255, 0, 0), 3)

cv2.imshow("dede", img)
cv2.waitKey(0)
"""

"""x, y, w, h = cv2.boundingRect(contours[0])
img2 = cv2.rectangle(img.copy(), (x, y), (x+w, y+h), (0,0,255), 2)

rect = cv2.minAreaRect(contours[0])
box = cv2.boxPoints(rect)
box = np.int64(box)
img2 = cv2.drawContours(img2, [box], 0, (0, 0, 255), 2)
"""

####################################
"""
def perspective_transform(image, corners):
    def order_corner_points(corners):
        # Separate corners into individual points
        # Index 0 - top-right
        #       1 - top-left
        #       2 - bottom-left
        #       3 - bottom-right
        corners = [(corner[0][0], corner[0][1]) for corner in corners]
        top_r, top_l, bottom_l, bottom_r = corners[0], corners[1], corners[2], corners[3]
        return (top_l, top_r, bottom_r, bottom_l)

    # Order points in clockwise order
    ordered_corners = order_corner_points(corners)
    top_l, top_r, bottom_r, bottom_l = ordered_corners

    # Determine width of new image which is the max distance between
    # (bottom right and bottom left) or (top right and top left) x-coordinates
    width_A = np.sqrt(((bottom_r[0] - bottom_l[0]) ** 2) + ((bottom_r[1] - bottom_l[1]) ** 2))
    width_B = np.sqrt(((top_r[0] - top_l[0]) ** 2) + ((top_r[1] - top_l[1]) ** 2))
    width = max(int(width_A), int(width_B))

    # Determine height of new image which is the max distance between
    # (top right and bottom right) or (top left and bottom left) y-coordinates
    height_A = np.sqrt(((top_r[0] - bottom_r[0]) ** 2) + ((top_r[1] - bottom_r[1]) ** 2))
    height_B = np.sqrt(((top_l[0] - bottom_l[0]) ** 2) + ((top_l[1] - bottom_l[1]) ** 2))
    height = max(int(height_A), int(height_B))

    # Construct new points to obtain top-down view of image in
    # top_r, top_l, bottom_l, bottom_r order
    dimensions = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1],
                    [0, height - 1]], dtype = "float32")

    # Convert to Numpy format
    ordered_corners = np.array(ordered_corners, dtype="float32")

    # Find perspective transform matrix
    matrix = cv2.getPerspectiveTransform(ordered_corners, dimensions)

    # Return the transformed image
    return cv2.warpPerspective(image, matrix, (width, height))

image = cv2.imread("./Full game areas/Single Board Area/OneBoard1.png")
original = image.copy()
blur = cv2.bilateralFilter(image,9,75,75)
gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray,40,255, cv2.THRESH_BINARY_INV)[1]

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

mask = np.zeros(image.shape, dtype=np.uint8)
for c in cnts:
    area = cv2.contourArea(c)
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.015 * peri, True)

    if area > 150000 and len(approx) == 4:
        cv2.drawContours(image,[c], 0, (36,255,12), 3)
        cv2.drawContours(mask,[c], 0, (255,255,255), -1)
        transformed = perspective_transform(original, approx)

transformed = perspective_transform(original, approx)
mask = cv2.bitwise_and(mask, original)

cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('transformed', transformed)
cv2.waitKey()"""

####################################

"""# convert the image to grayscale, blur it, and find edges
# in the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)

# find contours in the edged image, keep only the largest
# ones, and initialize our screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

# loop over our contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.015 * peri, True)
	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break
        
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3) 
cv2.imshow("Game Boy Screen", image) 
cv2.waitKey(0)"""

####################################

img = cv2.imread("./Full game areas/Single Board Area/OneBoard1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1, 1), np.uint64)

gray = cv2.bilateralFilter(gray, 13, 17, 3)
median = cv2.medianBlur(gray, 27)
blur = cv2.GaussianBlur(median, (47, 47), 1)
img_dilation = cv2.dilate(blur, kernel, iterations=3)
edged = cv2.Canny(img_dilation, 17, 17)
#dst = cv2.cornerHarris(edged, 7, 7, 0.006)
#dst = cv2.dilate(dst, None)

edged1 = edged
edged2 = edged
edged3 = edged
edged4 = edged

line1 = cv2.HoughLines(edged1,1,np.pi/30,159)
line2 = cv2.HoughLines(edged2,1,np.pi/300,159)
line3 = cv2.HoughLines(edged3,1,np.pi/200,159)
line4 = cv2.HoughLines(edged4,1,np.pi/80,159)
Lines = [line1, line2, line3, line4]

for line in Lines:
    for rho, theta in line[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        Newimg = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("Game Boy Screen", Newimg)
cv2.waitKey(0)

NewimgGray = cv2.cvtColor(Newimg, cv2.COLOR_BGR2GRAY)

cnts = cv2.findContours(NewimgGray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
"""cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None

# loop over our contours
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.015 * peri, True)
	# if our approximated contour has four points, then
	# we can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break"""

cv2.drawContours(Newimg, [cnts], -1, (0, 255, 0), 3)

cv2.imshow("Game Boy Screen", img)
cv2.waitKey(0)