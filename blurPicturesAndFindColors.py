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
    imgBlurred = cv2.medianBlur(img, 97)
    # cv2.imshow("Blurred", imgBlurred)
    # cv2.waitKey(0)

    avrColorByRow = np.average(imgBlurred, axis=0)
    avrColor = np.average(avrColorByRow, axis=0)

    return avrColor

def isColor(lower, upper, avgColor):
    if lower[0] <= avgColor[0] <= upper[0] and lower[1] <= avgColor[1] <= upper[1] and lower[2] <= avgColor[2] <= upper[2]:
        return True
    else:
        return False

# All the spectrums are based on the average colors (look at picture in report) where i took the lowest number -3 or highest number +3
def desertColor(img):

    desert_lower = np.array([41, 83, 95], np.uint8)
    desert_upper = np.array([59, 91, 102], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(desert_lower, desert_upper, color)

    return insideOrNot


def mineColor(img):
    mine_lower = np.array([20, 32, 38], np.uint8)
    mine_upper = np.array([28, 40, 46], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(mine_lower, mine_upper, color)

    return insideOrNot


def fieldColor(img):
    field_lower = np.array([44, 134, 153], np.uint8)
    field_upper = np.array([54, 157, 177], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(field_lower, field_upper, color)

    return insideOrNot


def forrestColor(img):
    forrest_lower = np.array([23, 58, 47], np.uint8)
    forrest_upper = np.array([29, 65, 62], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(forrest_lower, forrest_upper, color)

    return insideOrNot


def plainColor(img):
    plain_lower = np.array([42, 118, 92], np.uint8)
    plain_upper = np.array([57, 153, 119], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(plain_lower, plain_upper, color)

    return insideOrNot


def waterColor(img):
    water_lower = np.array([117, 70, 29], np.uint8)
    water_upper = np.array([175, 91, 47], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(water_lower, water_upper, color)

    return insideOrNot


def RColor(img):
    Red_lower = np.array([76, 93, 115], np.uint8)
    Red_upper = np.array([82, 99, 121], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(Red_lower, Red_upper, color)

    return insideOrNot

def RtowerColor(img):
    towerRed_lower = np.array([43, 57, 73], np.uint8)
    towerRed_upper = np.array([49, 63, 79], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(towerRed_lower, towerRed_upper, color)

    return insideOrNot

def BColor(img):
    Blue_lower = np.array([101, 105, 98], np.uint8)
    Blue_upper = np.array([107, 111, 104], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(Blue_lower, Blue_upper, color)

    return insideOrNot

def BtowerColor(img):
    towerBlue_lower = np.array([60, 67, 64], np.uint8)
    towerBlue_upper = np.array([66, 73, 70], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(towerBlue_lower, towerBlue_upper, color)

    return insideOrNot

def GColor(img):
    Green_lower = np.array([92, 115, 108], np.uint8)
    Green_upper = np.array([98, 121, 114], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(Green_lower, Green_upper, color)

    return insideOrNot

def GtowerColor(img):
    towerGreen_lower = np.array([47, 61, 55], np.uint8)
    towerGreen_upper = np.array([53, 67, 61], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(towerGreen_lower, towerGreen_upper, color)

    return insideOrNot

def YColor(img):
    Yellow_lower = np.array([78, 128, 129], np.uint8)
    Yellow_upper = np.array([84, 134, 135], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(Yellow_lower, Yellow_upper, color)

    return insideOrNot

def YtowerColor(img):
    towerYellow_lower = np.array([27, 55, 56], np.uint8)
    towerYellow_upper = np.array([33, 61, 62], np.uint8)
    color = np.array(find_avg_color(img))

    insideOrNot = isColor(towerYellow_lower, towerYellow_upper, color)

    return insideOrNot



def check_color(img):
    match = True

    if match == desertColor(img):
        result = "desert"
    elif match == mineColor(img):
        result = "mine"
    elif match == fieldColor(img):
        result = "field"
    elif match == forrestColor(img):
        result = "forrest"
    elif match == plainColor(img):
        result = "plain"
    elif match == waterColor(img):
        result = "water"
    elif match == RColor(img):
        result = "red"
    elif match == RtowerColor(img):
        result = "red"
    elif match == BColor(img):
        result = "blue"
    elif match == BtowerColor(img):
        result = "blue"
    elif match == GColor(img):
        result = "green"
    elif match == GtowerColor(img):
        result = "green"
    elif match == YColor(img):
        result = "yellow"
    elif match == YtowerColor(img):
        result = "yellow"
    else:
        result = "no match"

    print(find_avg_color(img))
    return result

"""check_color(img)
print(find_avg_color(img))
print(check_color(img))"""