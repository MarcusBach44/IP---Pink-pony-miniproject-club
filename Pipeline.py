import cv2

from find_crowns import find_crowns
from seperateSquares import SeperatesTiles
import groupTiles as groupTiles
import blurPicturesAndFindColors as color

img = cv2.imread("./Cropped and perspective corrected boards/1.jpg")
templateCrown = cv2.imread('./Crown Images/crown4.jpg')

ListOfAreas = []

#Separate Tiles into a list, going from 0-24
tiles = SeperatesTiles(img)
tileNumber = 0
groupTiles.possibleTiles()

#Looks through each tile for crowns, the stores each tile's amount of crowns in a list,
#going from 0-24 matching the tiles list
tilesCrownCount = []
for tile in tiles:
    tileNumber += 1
    # Looks through all tiles to find crowns
    tilesCrownCount.append(find_crowns(tile, templateCrown))

    # Defines tile area
    ListOfAreas.append(color.check_color(tile))








    """area = color.check_color(tile)
    areaAndNumber = area + str(tileNumber) + " "
    listHolder.append(list([areaAndNumber]))"""

    # Looks through all tiles to find groups, separates each group into a list
    """listHolder.append(groupTiles.CheckNeighbors(tileNumber, tiles, area, areaAndNumber))

    # Show tile
    cv2.imshow("tile", tile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

groupTiles.NewCheck(listHolder)"""

print (ListOfAreas)
