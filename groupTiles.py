import numpy as np
import cv2
import blurPicturesAndFindColors as colorFinder

img = cv2.imread("./Game pieces/Forest.png")

def categorizeArea(img):
    matches = colorFinder.check_color(img)

    match matches:
        case "desert":
            result = "desert"
        case "mine":
            result = "mine"
        case "field":
            result = "field"
        case "forrest":
            result = "forrest"
        case "plain":
            result = "plain"
        case "water":
            result = "water"

    return matches

##########################################################

def divideIntoLists(img):
    Category = categorizeArea(img)

    for area in range(25):


        return

    return

print(categorizeArea(img))