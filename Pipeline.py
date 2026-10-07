import cv2

from find_crowns import find_crowns
from seperateSquares import SeperatesTiles
import blurPicturesAndFindColors as color

img = cv2.imread("./Cropped and perspective corrected boards/2.jpg")
templateCrown = cv2.imread('./Crown Images/crown4.jpg')

#Separate Tiles into a list, going from 0-24
tiles = SeperatesTiles(img)

#Looks through each tile for crowns, the stores each tile's amount of crowns in a list,
#going from 0-24 matching the tiles list
tilesCrownCount = []
for tile in tiles:
    #tilesCrownCount.append(find_crowns(tile, templateCrown))
    print(color.check_color(tile))
    #cv2.imshow("tile", tile)
    #cv2.waitKey(0)

#Looks through all tiles to find groups, separates each group into a list


