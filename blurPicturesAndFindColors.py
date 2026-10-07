import numpy as np
import cv2

img = cv2.imread("./Game pieces/Blue tower.png")

imgBlurred = cv2.medianBlur(img, 97)
#cv2.imshow("Blurred", imgBlurred)
#cv2.waitKey(0)

avrColorByRow = np.average(imgBlurred, axis=0)
avrColor = np.average(avrColorByRow, axis=0)



#Keep in mind at den printer det som BGR, fordi selvfølgelig gør den det  ._.
print(avrColor)

# All the spectrums are based on the average colors (look at picture in report) where i took the lowest number -3 or highest number +3
def desertColor(img):
    classification = False

    desert_lower = np.array([41, 83, 95], np.uint8)
    desert_upper = np.array([59, 91, 102], np.uint8)

    desert_sectrum = cv2.inRange(img, desert_lower, desert_upper)
    if avrColor in desert_sectrum:
        classification = True

    return classification


def mineColor(img):
    classification = False

    mine_lower = np.array([20, 32, 38], np.uint8)
    mine_upper = np.array([28, 40, 46], np.uint8)

    mine_spectrum = cv2.inRange(img, mine_lower, mine_upper)
    if avrColor in mine_spectrum:
        classification = True

    return classification


def fieldColor(img):
    classification = False

    field_lower = np.array([44, 134, 153], np.uint8)
    field_upper = np.array([54, 157, 177], np.uint8)

    field_spectrum = cv2.inRange(img, field_lower, field_upper)
    if avrColor in field_spectrum:
        classification = True

    return classification


def forrestColor(img):
    classification = False

    forrest_lower = np.array([23, 58, 47], np.uint8)
    forrest_upper = np.array([29, 65, 62], np.uint8)

    forrest_spectrum = cv2.inRange(img, forrest_lower, forrest_upper)
    if avrColor in forrest_spectrum:
        classification = True

    return classification


def plainColor(img):
    classification = False

    plain_lower = np.array([42, 118, 92], np.uint8)
    plain_upper = np.array([57, 153, 119], np.uint8)

    plain_spectrum = cv2.inRange(img, plain_lower, plain_upper)
    if avrColor in plain_spectrum:
        classification = True

    return classification


def waterColor(img):
    classification = False

    water_lower = np.array([117, 70, 29], np.uint8)
    water_upper = np.array([175, 91, 47], np.uint8)

    water_spectrum = cv2.inRange(img, water_lower, water_upper)
    if avrColor in water_spectrum:
        classification = True

    return classification


def towerColor(img):
    classification = False

    Red_lower = np.array([76, 93, 115], np.uint8)
    Red_upper = np.array([82, 99, 121], np.uint8)
    Red_spectrum = cv2.inRange(img, Red_lower, Red_upper)

    towerRed_lower = np.array([43, 57, 73], np.uint8)
    towerRed_upper = np.array([49, 63, 79], np.uint8)
    towerRed_spectrum = cv2.inRange(img, towerRed_lower, towerRed_upper)

    Blue_lower = np.array([101, 105, 98], np.uint8)
    Blue_upper = np.array([107, 111, 104], np.uint8)
    Blue_spectrum = cv2.inRange(img, Blue_lower, Blue_upper)

    towerBlue_lower = np.array([60, 67, 64], np.uint8)
    towerBlue_upper = np.array([66, 73, 70], np.uint8)
    towerBlue_spectrum = cv2.inRange(img, towerBlue_lower, towerBlue_upper)

    Green_lower = np.array([92, 115, 108], np.uint8)
    Green_upper = np.array([98, 121, 114], np.uint8)
    Green_spectrum = cv2.inRange(img, Green_lower, Green_upper)

    towerGreen_lower = np.array([47, 61, 55], np.uint8)
    towerGreen_upper = np.array([53, 67, 61], np.uint8)
    towerGreen_spectrum = cv2.inRange(img, towerGreen_lower, towerGreen_upper)

    Yellow_lower = np.array([78, 128, 129], np.uint8)
    Yellow_upper = np.array([84, 134, 135], np.uint8)
    Yellow_spectrum = cv2.inRange(img, Yellow_lower, Yellow_upper)

    towerYellow_lower = np.array([27, 55, 56], np.uint8)
    towerYellow_upper = np.array([33, 61, 62], np.uint8)
    towerYellow_spectrum = cv2.inRange(img, towerYellow_lower, towerYellow_upper)

    if avrColor in towerRed_spectrum or towerBlue_spectrum or towerGreen_spectrum or towerYellow_spectrum or Red_spectrum or Blue_spectrum or Green_spectrum or Yellow_spectrum:
        classification = True

    return classification