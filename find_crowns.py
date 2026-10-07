import cv2
import numpy as np

from seperateSquares import SeperatesTiles

#image = cv2.imread("./Cropped and perspective corrected boards/14.jpg")
#cv2.imshow("Original", image)

#crown_img = cv2.imread("Crown Images/crown4.jpg")

#cv2.imshow("Crown", crown_img)

def create_template_array(template):
    template_array = [
        template,
        cv2.rotate(template, cv2.ROTATE_90_CLOCKWISE),
        cv2.rotate(template, cv2.ROTATE_180),
        cv2.rotate(template, cv2.ROTATE_90_COUNTERCLOCKWISE)
    ]
    return template_array

def convert_array_grayscale(img_array):
    new_array = []
    for img in img_array:
        new_array.append(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    return new_array


def find_crowns(img, crowns):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Crowns", img_gray)
    template_array_grayscale = convert_array_grayscale(create_template_array(crowns))
    amount_of_crowns = 0
    previous_crown = (-50, -50)
    previous_crowns2 = (-50, -50)

    match_found = False
    for template in template_array_grayscale:
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.6
        loc = np.where(res >= threshold)
        #cv2.destroyAllWindows()
        #cv2.imshow("Crowns", template)
        #cv2.imshow("image", img)
        #cv2.waitKey(0)

        for pt in zip(*loc[::-1]):
            if ((pt[0] < previous_crown[0] and
                 (pt[0]+w < previous_crown[0] or pt[1] > previous_crown[1]+h) and
                    (pt[0]+w < previous_crowns2[0] or pt[1] > previous_crowns2[1]+h))
            or (pt[0] > previous_crown[0] and
                (pt[0] > previous_crown[0]+w or pt[1] > previous_crown[1]+h) and
                    (pt[0] > previous_crowns2[0]+w or pt[1] > previous_crowns2[1]+h))
            or (pt[0] == previous_crown[0] and pt[1] > previous_crown[1]+h) and
                    (pt[0] == previous_crowns2[0] and pt[1] > previous_crowns2[1]+h)):
                """"
                if ((pt[0] < previous_crown[0]-1 and pt[1] > previous_crowns2[1]+2)
                or (pt[0] > previous_crown[0]+w and pt[1] >= previous_crowns2[1]+1)
                or (pt[0] == previous_crown[0] and pt[1] > previous_crown[1]+h)
                or (pt[1] > previous_crown[1]+h)
                or (pt[1] < previous_crown[1])):
                """
                match_found = True
                img = cv2.rectangle(img, pt, (pt[0] + w, pt[1]+h), (0, 255, 0), 2)
                amount_of_crowns += 1
                #print("Previous Crown Pos: ",previous_crown[0], previous_crown[1], " New Crown Pos: ", pt[0], pt[1])
                #print("Size of crown", w, h)
                previous_crowns2 = previous_crown
                previous_crown = pt

                #cv2.imshow("Crowns", template)
                #cv2.imshow("image", img)
                #cv2.waitKey(0)

        if match_found:
            break
    print("Amount of Crowns: ", amount_of_crowns)
    return amount_of_crowns

"""
amount_of_crowns = find_crowns(image, create_template_array(crown_img))
print("Amount of Crowns: ", amount_of_crowns)
cv2.imshow("Crowns on board", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""