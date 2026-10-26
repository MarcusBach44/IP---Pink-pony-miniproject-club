import cv2

from find_crowns import find_crowns_in_group
from seperateSquares import SeperatesTiles
from blurPicturesAndFindColors import define_tiles
from groupTiles import grass_fire_algorithm
from HomographyOfGameBoard import ScaleBoardIsh

#Here is the pipeline for scaling the board and finding points
def pipeline_scale_board():
    img = cv2.imread("./Full game areas/Single Board Area/OneBoard1.png")
    templateCrown1 = cv2.imread('./Crown Images/crown14.png')
    templateCrown2 = cv2.imread('./Crown Images/crown14.2.png')
    templateCrown3 = cv2.imread('./Crown Images/crown14.3.png')
    templateCrown4 = cv2.imread('./Crown Images/crown14.4.png')
    templateCrowns = [templateCrown1, templateCrown2, templateCrown3, templateCrown4]
    totalPoints = 0

    # it works with 1 board, no touchy, it will break i swear
    scaled = ScaleBoardIsh(img)

    # Separate Tiles into a list, going from 0-24
    tiles = SeperatesTiles(scaled)

    # Assign each tile its type
    listOfAreas = define_tiles(tiles)

    # Create lists with each grouping of tiles
    listOfGroups = grass_fire_algorithm(listOfAreas)
    print(listOfGroups)

    # Find crowns in each grouping and calculate points
    for group in listOfGroups:
        amountOfCrowns = find_crowns_in_group(group, tiles, templateCrowns, 0.78)
        totalPoints += amountOfCrowns * len(group)
    print(totalPoints)


#Here is the pipeline, which can be used for ALREADY scaled images of game boards
def pipeline():
    img = cv2.imread("./Cropped and perspective corrected boards/2.jpg")
    templateCrown1 = cv2.imread('./Crown Images/crown4.jpg')
    templateCrowns = [templateCrown1]
    totalPoints = 0

    tiles = SeperatesTiles(img)

    # Assign each tile its type
    listOfAreas = define_tiles(tiles)
    print(listOfAreas)

    # Create lists with each grouping of tiles
    listOfGroups = grass_fire_algorithm(listOfAreas)

    # Find crowns in each grouping and calculate points
    for group in listOfGroups:
        amountOfCrowns = find_crowns_in_group(group, tiles, templateCrowns, 0.6)
        totalPoints += amountOfCrowns * len(group)
    print(totalPoints)

#######################################

pipeline_scale_board()
#pipeline()
