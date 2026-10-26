from unittest import result, case
from xml.etree.ElementTree import tostring

import numpy as np
import cv2

def find_avg_color(img):
    avrColorByRow = np.average(img, axis=0)
    avrColor = np.average(avrColorByRow, axis=0)
    return avrColor

def manipulateImg(img):
    imgMedianBlur = cv2.medianBlur(img, 97)
    imgGaussianBlur = cv2.GaussianBlur(imgMedianBlur, (55, 55), 0)
    return imgGaussianBlur

def brightenImg(img):
    cvtImg = cv2.convertScaleAbs(img, alpha= 1.4, beta= 1)
    return cvtImg

def Color(lower, upper, img):
    color = np.array(find_avg_color(img))
    lower = lower
    upper = upper
    isColorTorF = isColor(lower, upper, color)
    return isColorTorF

def isColor(lower, upper, avgColor):
    if lower[0] <= avgColor[0] <= upper[0] and lower[1] <= avgColor[1] <= upper[1] and lower[2] <= avgColor[2] <= upper[2]:
        return True
    else:
        return False

def areaFunctions(img):
    ColorFunctions = [desertColor(img), mineColor(img), fieldColor(img), forrestColor(img), plainColor(img),
                      waterColor(img),
                      RColor(img), RtowerColor(img),
                      BColor(img), BtowerColor(img),
                      GColor(img), GtowerColor(img),
                      YColor(img), YtowerColor(img)]
    return ColorFunctions

def areaNames():
    ColorAreas = ["desert ", "mine ", "field ", "forrest ", "plain ", "water ",
                  "Red ", "Redtower ",
                  "Blue ", "Bluetower ",
                  "Green ", "Greentower ",
                  "Yellow ", "Yellowtower ",]
    return ColorAreas

#################################################

# All the spectrum are based on the average colors (look at picture in report)
def desertColor(img):
    desert_lower = np.array([30, 90, 100], np.uint8)
    desert_upper = np.array([135, 190, 205], np.uint8)
    result = Color(desert_lower, desert_upper, img)
    return result

def mineColor(img):
    mine_lower = np.array([15, 50, 50], np.uint8)
    mine_upper = np.array([70, 100, 130], np.uint8)
    result = Color(mine_lower, mine_upper, img)
    return result

def fieldColor(img):
    field_lower = np.array([1, 160, 180], np.uint8)
    field_upper = np.array([90, 255, 255], np.uint8)
    result = Color(field_lower, field_upper, img)
    return result

def forrestColor(img):
    forrest_lower = np.array([13, 50, 30], np.uint8)
    forrest_upper = np.array([85, 175, 135], np.uint8)
    result = Color(forrest_lower, forrest_upper, img)
    return result

def plainColor(img):
    plain_lower = np.array([10, 145, 105], np.uint8)
    plain_upper = np.array([94, 240, 200], np.uint8)
    result = Color(plain_lower, plain_upper, img)
    return result

def waterColor(img):
    water_lower = np.array([90, 80, 1], np.uint8)
    water_upper = np.array([254, 160, 130], np.uint8)
    result = Color(water_lower, water_upper, img)
    return result

def RColor(img):
    Red_lower = np.array([79, 96, 118], np.uint8)
    Red_upper = np.array([79, 96, 118], np.uint8)
    result = Color(Red_lower, Red_upper, img)
    return result

def RtowerColor(img):
    towerRed_lower = np.array([46, 60, 76], np.uint8)
    towerRed_upper = np.array([46, 60, 76], np.uint8)
    result = Color(towerRed_lower, towerRed_upper, img)
    return result

def BColor(img):
    Blue_lower = np.array([130, 135, 120], np.uint8)
    Blue_upper = np.array([145, 150, 135], np.uint8)
    result = Color(Blue_lower, Blue_upper, img)
    return result

def BtowerColor(img):
    towerBlue_lower = np.array([63, 70, 67], np.uint8)
    towerBlue_upper = np.array([63, 70, 67], np.uint8)
    result = Color(towerBlue_lower, towerBlue_upper, img)
    return result

def GColor(img):
    Green_lower = np.array([95, 118, 111], np.uint8)
    Green_upper = np.array([95, 118, 111], np.uint8)
    result = Color(Green_lower, Green_upper, img)
    return result

def GtowerColor(img):
    towerGreen_lower = np.array([50, 64, 58], np.uint8)
    towerGreen_upper = np.array([50, 64, 58], np.uint8)
    result = Color(towerGreen_lower, towerGreen_upper, img)
    return result

def YColor(img):
    Yellow_lower = np.array([85, 195, 195], np.uint8)
    Yellow_upper = np.array([100, 210, 210], np.uint8)
    result = Color(Yellow_lower, Yellow_upper, img)
    return result

def YtowerColor(img):
    towerYellow_lower = np.array([70, 140, 140], np.uint8)
    towerYellow_upper = np.array([100, 160, 160], np.uint8)
    result = Color(towerYellow_lower, towerYellow_upper, img)
    return result

#################################################

def FindBiggestChange(img, newImg):
    B1 = find_avg_color(img)[0]
    B2 = find_avg_color(newImg)[0]

    G1 = find_avg_color(img)[0]
    G2 = find_avg_color(newImg)[1]

    R1 = find_avg_color(img)[0]
    R2 = find_avg_color(newImg)[2]

    B = B2 - B1
    G = G2 - G1
    R = R2 - R1

    biggestValue = max(B, G, R)
    bigVal = 0

    if biggestValue == B:
        bigVal = 1
    if biggestValue == G:
        bigVal = 2
    if biggestValue == R:
        bigVal = 3

    return bigVal

def check_color(img):
    matchesFound = 0
    num = 0

    newImg = brightenImg(img)
    newImg = manipulateImg(newImg)

    aName = areaNames()
    aFunc = areaFunctions(newImg)
    matches = ""
    result = ""

    for function in aFunc:
        if function == True:
            matchesFound = matchesFound + 1
            matches = matches + aName[num]
        num = num + 1

    biggestValue = FindBiggestChange(img, newImg)

    match matches:
        case "desert ":
            result = "desert"
        case "mine ":
            result = "mine"
        case "field ":
            result = "field"
        case "forrest ":
            result = "forrest"
        case "plain ":
            result = "plain"
        case "water ":
            result = "water"


        case "desert mine forrest ":
            if biggestValue == 1:
                result = "blue"
                print("desert mine forrest - no type")
            elif biggestValue == 2:
                result = "forrest"
            elif biggestValue == 3:
                result = "desert"

        case "desert forrest plain ":
            if biggestValue == 1:
                result = "blue"
                print("desert forrest plain - no type")
            elif biggestValue == 2:
                result = "plain"
            elif biggestValue == 3:
                result = "red"
                print("desert forrest plain - no type")

        case "mine forrest ":
            if biggestValue == 1:
                result = "blue"
                print("mine forrest - no type")
            elif biggestValue == 2:
                result = "forrest"
            elif biggestValue == 3:
                result = "mine"

        case "desert mine ":
            if biggestValue == 1:
                result = "blue"
                print("desert mine - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert mine - no type")
            elif biggestValue == 3:
                result = "red"
                print("desert mine - no type")

        case "forrest plain ":
            if biggestValue == 1:
                result = "blue"
                print("forrest plain - no type")
            elif biggestValue == 2:
                result = "plain"
            elif biggestValue == 3:
                result = "red"
                print("forrest plain - no type")

        case "desert forrest ":
            if biggestValue == 1:
                result = "blue"
                print("desert forrest - no type")
            elif biggestValue == 2:
                result = "forrest"
            elif biggestValue == 3:
                result = "desert"

        case "field plain ":
            if biggestValue == 1:
                result = "blue"
                print("field plain - no type")
            elif biggestValue == 2:
                result = "plain"
            elif biggestValue == 3:
                result = "field"

        case "desert plain ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain - no type")
            elif biggestValue == 2:
                result = "plain"
            elif biggestValue == 3:
                result = "desert"

        case "desert plain Yellowtower ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain Yellowtower - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert plain Yellowtower - no type")
            elif biggestValue == 3:
                result = "crown"

        case "desert plain Yellow ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain Yellow - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert plain Yellow - no type")
            elif biggestValue == 3:
                result = "red"
                print("desert plain Yellow - no type")

        case "desert plain Greentower ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain Greentower - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert plain Greentower - no type")
            elif biggestValue == 3:
                result = "red"
                print("desert plain Greentower - no type")

        case "desert plain Green ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain Green - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert plain Green - no type")
            elif biggestValue == 3:
                result = "red"
                print("desert plain Green - no type")

        case "desert plain Bluetower ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain Bluetower - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert plain Bluetower - no type")
            elif biggestValue == 3:
                result = "red"
                print("desert plain Bluetower - no type")

        case "desert plain Blue ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain Blue - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert plain Blue - no type")
            elif biggestValue == 3:
                result = "red"
                print("desert plain Blue - no type")

        case "desert plain Redtower ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain Redtower - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert plain Redtower - no type")
            elif biggestValue == 3:
                result = "red"
                print("desert plain Redtower - no type")

        case "desert plain Red ":
            if biggestValue == 1:
                result = "blue"
                print("desert plain Red - no type")
            elif biggestValue == 2:
                result = "green"
                print("desert plain Red - no type")
            elif biggestValue == 3:
                result = "red"
                print("desert plain Red - no type")

    return result

def define_tiles(tiles):
    ListOfAreas = []
    for tile in tiles:
        ListOfAreas.append(check_color(tile))
        """print(check_color(tile))
        cv2.imshow("tile", tile)
        cv2.waitKey(0)"""

    return ListOfAreas