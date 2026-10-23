import cv2

from find_crowns import find_crowns_in_group
from seperateSquares import SeperatesTiles
from blurPicturesAndFindColors import define_tiles
from groupTiles import grass_fire_algorithm
from HomographyOfGameBoard import ScaleBoardIsh

img = cv2.imread("./Full game areas/Single Board Area/OneBoard1.png")
templateCrown = cv2.imread('./Crown Images/crown5.jpg')
totalPoints = 0

#it works with 1 board, no touchy, it will break i swear
scaled = ScaleBoardIsh(img)

#Separate Tiles into a list, going from 0-24
tiles = SeperatesTiles(scaled)

#Assign each tile its type
listOfAreas = define_tiles(tiles)
print(listOfAreas)

#Create lists with each grouping of tiles
listOfGroups = grass_fire_algorithm(listOfAreas)
print(listOfGroups)

#Find crowns in each grouping and calculate points
for group in listOfGroups:
    amountOfCrowns = find_crowns_in_group(group, tiles, templateCrown)
    totalPoints += amountOfCrowns * len(group)
    print("group: ",group,"" " = Crowns: ", amountOfCrowns, "*", " Size: ",len(group)," = ", totalPoints)
print(totalPoints)
