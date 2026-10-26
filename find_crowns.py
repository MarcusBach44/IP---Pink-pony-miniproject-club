import cv2
import numpy as np

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


def find_crowns(img, crownTemplates):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template_array_grayscale = []
    for template in crownTemplates:
        for temp in convert_array_grayscale(create_template_array(template)):
            template_array_grayscale.append(temp)
    amount_of_crowns = 0
    previous_crown = (-50, -50)
    previous_crowns2 = (-50, -50)

    match_found = False
    for template in template_array_grayscale:
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.78
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

                match_found = True
                img = cv2.rectangle(img, pt, (pt[0] + w, pt[1]+h), (0, 255, 0), 2)
                amount_of_crowns += 1
                #print("Previous Crown Pos: ",previous_crown[0], previous_crown[1], " New Crown Pos: ", pt[0], pt[1])
                #print("Size of crown", w, h)
                previous_crowns2 = previous_crown
                previous_crown = pt

                cv2.imshow("Crowns", template)
                cv2.imshow("image", img)
                cv2.waitKey(0)

        if match_found:
            break
    #print("Amount of Crowns: ", amount_of_crowns)
    return amount_of_crowns

def find_crowns_in_group(group, tiles, template):
    amount_of_crowns = 0
    for tileIndex in group:
        img = tiles[tileIndex]
        amount_of_crowns += find_crowns(img, template)
    return amount_of_crowns

"""
amount_of_crowns = find_crowns(image, create_template_array(crown_img))
print("Amount of Crowns: ", amount_of_crowns)
cv2.imshow("Crowns on board", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""