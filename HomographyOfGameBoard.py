import numpy as np
import imutils
import cv2

def ScaleBoardIsh(Img):

    OriginalImg = Img
    whiteImg = Img
    whiteImg = cv2.cvtColor(whiteImg, cv2.COLOR_BGR2GRAY)
    whiteImg = cv2.convertScaleAbs(whiteImg, alpha=30, beta=70)

    height, width, channels = OriginalImg.shape

    img = Img
    cvtImg = cv2.convertScaleAbs(img, alpha=1.3, beta=5)
    gray = cv2.cvtColor(cvtImg, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint64)

    gray = cv2.bilateralFilter(gray, 13, 17, 3)
    median = cv2.medianBlur(gray, 37)
    blur = cv2.GaussianBlur(median, (47, 47), 1)
    img_dilation = cv2.dilate(blur, kernel, iterations=3)
    edged = cv2.Canny(img_dilation, 17, 17)

    edged1 = edged
    edged2 = edged
    edged3 = edged
    edged4 = edged

    lineRight = cv2.HoughLines(edged1,1,np.pi/30,1)
    lineTop = cv2.HoughLines(edged2,1,np.pi/500,1)
    line3 = cv2.HoughLines(edged3,1,np.pi/200,1)
    lineBottom = cv2.HoughLines(edged4,1,np.pi/80,1)
    Lines = [lineRight, lineTop, line3, lineBottom]

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

            Newimg = cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 5)

    Newedged = cv2.Canny(Newimg, 17, 17)

    cnts = cv2.findContours(Newedged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
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

    cv2.drawContours(whiteImg, [screenCnt], -1, (0, 255, 0), 3)

    corners = cv2.goodFeaturesToTrack(whiteImg, 4, 0.1, 10)
    corners = np.int16(corners)
    cornersArr = []

    for i in corners:
        x, y = i.ravel()
        cv2.circle(OriginalImg, (x, y), 5, 255, -1)
        cornersArr.append(x)
        cornersArr.append(y)

    print(cornersArr)

    topleftX = int(cornersArr[1])
    topleftY = int(cornersArr[0])

    toprightX = int(cornersArr[3])
    toprightY = int(cornersArr[2])

    bottomleftX = int(cornersArr[5])
    bottomleftY = int(cornersArr[4])

    bottomRightX = int(cornersArr[7])
    bottomRightY = int(cornersArr[6])

    original_points = np.array([[topleftY, topleftX], [bottomleftY, bottomleftX], [bottomRightY, bottomRightX], [toprightY, toprightX]], dtype=np.float32)
    target_points = np.array([[0, 0], [0, height], [width, height], [width, 0]], dtype=np.float32)

    mat = cv2.getPerspectiveTransform(original_points, target_points)
    perspective_image = cv2.warpPerspective(OriginalImg, mat, (width, height))

    return perspective_image





