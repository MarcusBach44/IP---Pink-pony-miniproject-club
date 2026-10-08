from unittest import result, case

import numpy as np
import cv2
from sympy import true


#img = cv2.imread("./Game pieces/Mine.png")

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
    mine_lower = np.array([15, 50, 60], np.uint8)
    mine_upper = np.array([70, 100, 130], np.uint8)
    result = Color(mine_lower, mine_upper, img)
    return result

def fieldColor(img):
    field_lower = np.array([1, 160, 180], np.uint8)
    field_upper = np.array([40, 255, 255], np.uint8)
    result = Color(field_lower, field_upper, img)
    return result

def forrestColor(img):
    forrest_lower = np.array([13, 50, 30], np.uint8)
    forrest_upper = np.array([85, 175, 135], np.uint8)
    result = Color(forrest_lower, forrest_upper, img)
    return result

def plainColor(img):
    plain_lower = np.array([10, 145, 105], np.uint8)
    plain_upper = np.array([70, 240, 200], np.uint8)
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
    towerYellow_lower = np.array([30, 58, 59], np.uint8)
    towerYellow_upper = np.array([30, 58, 59], np.uint8)
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
    PrintText = "Amount of matches based on color code: "
    matchesFound = 0
    num = 0
    newImg = brightenImg(img)
    newImg = manipulateImg(newImg)
    print(find_avg_color(newImg))

    aName = areaNames()
    aFunc = areaFunctions(newImg)
    matches = ""
    result = "High probability it is true"

    for function in aFunc:
        if function == True:
            matchesFound = matchesFound + 1
            matches = matches + aName[num]
        num = num + 1

    print(matches)

    if matchesFound > 1:
        biggestValue = FindBiggestChange(img, newImg)

        match matches:
            case "desert mine forrest ":
                if biggestValue == 1:
                    result = "should be blue"
                elif biggestValue == 2:
                    result = "should be forrest"
                elif biggestValue == 3:
                    result = "should be desert"

            case "desert forrest plain ":
                if biggestValue == 1:
                    result = "should be blue"
                elif biggestValue == 2:
                    result = "should be plain"
                elif biggestValue == 3:
                    result = "should be red"

            case "mine forrest ":
                if biggestValue == 1:
                    result = "should be blue"
                elif biggestValue == 2:
                    result = "should be forrest"
                elif biggestValue == 3:
                    result = "should be mine"

            case "desert mine ":
                if biggestValue == 1:
                    result = "should be blue"
                elif biggestValue == 2:
                    result = "should be green"
                elif biggestValue == 3:
                    result = "should be red"

            case "forrest plain ":
                if biggestValue == 1:
                    result = "idk blue"
                elif biggestValue == 2:
                    result = "should be plain"
                elif biggestValue == 3:
                    result = "idk red"

            case "desert forrest ":
                if biggestValue == 1:
                    result = "should be blue"
                elif biggestValue == 2:
                    result = "should be forrest"
                elif biggestValue == 3:
                    result = "should be desert"

            case "field plain ":
                if biggestValue == 1:
                    result = "should be blue"
                elif biggestValue == 2:
                    result = "should be plain"
                elif biggestValue == 3:
                    result = "should be field"

            case "desert plain ":
                if biggestValue == 1:
                    result = "should be blue"
                elif biggestValue == 2:
                    result = "should be plain"
                elif biggestValue == 3:
                    result = "should be desert"

    return PrintText, matchesFound, result

#def findArea(matchAmount, matchNames):
    matches = matchAmount
    names = matchNames
    result = ""

    match matches:
        case "desert mine forest ":
            result = "one"
        case "mine forest ":
            result = "two"
    return result

"""def check_color(img):
    print(find_avg_color(img))
    result = ""

    if desertColor(img):
        result = result + "desert "
    elif mineColor(img):
        result = result + "mine "
    elif fieldColor(img):
        result = result + "field "
    elif forrestColor(img):
        result = result + "forrest "
    elif plainColor(img):
        result = result + "plain "
    elif waterColor(img):
        result = result + "water "
    elif RColor(img):
        result = "red "
    elif RtowerColor(img):
        result = "redT "
    elif BColor(img):
        result = "blue "
    elif BtowerColor(img):
        result = "blueT "
    elif GColor(img):
        result = "green "
    elif GtowerColor(img):
        result = "greenT "
    elif YColor(img):
        result = "yellow "
    elif YtowerColor(img):
        result = "yellowT "
    else:
        result = "no match"


    return result"""

#check_color(img)
#FindBiggestChange(img)
#print(check_color(img))

#print(find_avg_color(img))
#print(FindBiggestChange(img))