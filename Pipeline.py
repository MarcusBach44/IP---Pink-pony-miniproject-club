import cv2

from find_crowns import find_crowns_in_group
from seperateSquares import SeperatesTiles
from blurPicturesAndFindColors import define_tiles
from groupTiles import grass_fire_algorithm
from HomographyOfGameBoard import ScaleBoardIsh

img = cv2.imread("./Full game areas/Single Board Area/OneBoard1.png")
templateCrown1 = cv2.imread('./Crown Images/crown14.png')
templateCrown2 = cv2.imread('./Crown Images/crown14.2.png')
templateCrown3 = cv2.imread('./Crown Images/crown14.3.png')
templateCrown4 = cv2.imread('./Crown Images/crown14.4.png')
templateCrowns = [templateCrown1, templateCrown2, templateCrown3, templateCrown4]
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
    amountOfCrowns = find_crowns_in_group(group, tiles, templateCrowns)
    totalPoints += amountOfCrowns * len(group)
    #print("group: ",group,"" " = Crowns: ", amountOfCrowns, "*", " Size: ",len(group)," = ", totalPoints)
print(totalPoints)
