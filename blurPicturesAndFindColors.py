from unittest import result

import numpy as np
import cv2

img = cv2.imread("./Crown Images/crown.jpg")

"""
imgBlurred = cv2.medianBlur(img, 97)
#cv2.imshow("Blurred", imgBlurred)
#cv2.waitKey(0)

avrColorByRow = np.average(imgBlurred, axis=0)
avrColor = np.average(avrColorByRow, axis=0)



#Keep in mind at den printer det som BGR, fordi selvfølgelig gør den det  ._.
print(avrColor)
"""

def find_avg_color(img):
    imgMedianBlur= cv2.medianBlur(img, 97)
    imgGaussianBlur = cv2.GaussianBlur(imgMedianBlur, (55, 55), 0)
    avrColorByRow = np.average(imgGaussianBlur, axis=0)
    avrColor = np.average(avrColorByRow, axis=0)
    return avrColor

def isColor(lower, upper, avgColor):
    if lower[0] <= avgColor[0] <= upper[0] and lower[1] <= avgColor[1] <= upper[1] and lower[2] <= avgColor[2] <= upper[2]:
        return True
    else:
        return False

def Color(lower, upper, img):
    color = np.array(find_avg_color(img))
    lower = lower
    upper = upper
    isColorTorF = isColor(lower, upper, color)
    return isColorTorF

def ifSame(img):



    return




# All the spectrum are based on the average colors (look at picture in report)
def desertColor(img):
    desert_lower = np.array([27, 71, 79], np.uint8)
    desert_upper = np.array([64, 110, 131], np.uint8)
    result = Color(desert_lower, desert_upper, img)
    return result

def mineColor(img):
    mine_lower = np.array([11, 30, 36], np.uint8)
    mine_upper = np.array([30, 67, 81], np.uint8)
    result = Color(mine_lower, mine_upper, img)
    return result

def fieldColor(img):
    field_lower = np.array([1, 126, 148], np.uint8)
    field_upper = np.array([56, 165, 187], np.uint8)
    result = Color(field_lower, field_upper, img)
    return result

def forrestColor(img):
    forrest_lower = np.array([14, 56, 45], np.uint8)
    forrest_upper = np.array([29, 65, 62], np.uint8)
    result = Color(forrest_lower, forrest_upper, img)
    return result

def plainColor(img):
    plain_lower = np.array([12, 112, 88], np.uint8)
    plain_upper = np.array([59, 155, 121], np.uint8)
    result = Color(plain_lower, plain_upper, img)
    return result

def waterColor(img):
    water_lower = np.array([113, 68, 10], np.uint8)
    water_upper = np.array([177, 94, 49], np.uint8)
    result = Color(water_lower, water_upper, img)
    return result

def RColor(img):
    Red_lower = np.array([73, 91, 113], np.uint8)
    Red_upper = np.array([84, 103, 123], np.uint8)
    result = Color(Red_lower, Red_upper, img)
    return result

def RtowerColor(img):
    towerRed_lower = np.array([45, 59, 75], np.uint8)
    towerRed_upper = np.array([51, 65, 81], np.uint8)
    result = Color(towerRed_lower, towerRed_upper, img)
    return result

def BColor(img):
    Blue_lower = np.array([99, 103, 96], np.uint8)
    Blue_upper = np.array([109, 113, 106], np.uint8)
    result = Color(Blue_lower, Blue_upper, img)
    return result

def BtowerColor(img):
    towerBlue_lower = np.array([58, 65, 62], np.uint8)
    towerBlue_upper = np.array([68, 75, 72], np.uint8)
    result = Color(towerBlue_lower, towerBlue_upper, img)
    return result

def GColor(img):
    Green_lower = np.array([90, 113, 106], np.uint8)
    Green_upper = np.array([100, 123, 116], np.uint8)
    result = Color(Green_lower, Green_upper, img)
    return result

def GtowerColor(img):
    towerGreen_lower = np.array([45, 59, 53], np.uint8)
    towerGreen_upper = np.array([55, 69, 63], np.uint8)
    result = Color(towerGreen_lower, towerGreen_upper, img)
    return result

def YColor(img):
    Yellow_lower = np.array([70, 126, 127], np.uint8)
    Yellow_upper = np.array([86, 136, 137], np.uint8)
    result = Color(Yellow_lower, Yellow_upper, img)
    return result

def YtowerColor(img):
    towerYellow_lower = np.array([25, 53, 54], np.uint8)
    towerYellow_upper = np.array([35, 63, 64], np.uint8)
    result = Color(towerYellow_lower, towerYellow_upper, img)
    return result



def check_color(img):
    print(find_avg_color(img))
    result = ""

    if desertColor(img):
        result += "desert "
    elif mineColor(img):
        result += "mine "
    elif fieldColor(img):
        result += "field "
    elif forrestColor(img):
        result += "forrest "
    elif plainColor(img):
        result += "plain "
    elif waterColor(img):
        result += "water "
    elif RColor(img):
        result += "red "
    elif RtowerColor(img):
        result += "redT "
    elif BColor(img):
        result += "blue "
    elif BtowerColor(img):
        result += "blueT "
    elif GColor(img):
        result += "green "
    elif GtowerColor(img):
        result += "greenT "
    elif YColor(img):
        result += "yellow "
    elif YtowerColor(img):
        result += "yellowT "
    else:
        result = "no match"


    return result

"""check_color(img)
print(find_avg_color(img))
print(check_color(img))"""