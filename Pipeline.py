import cv2

from find_crowns import find_crowns_in_group
from seperateSquares import SeperatesTiles
from blurPicturesAndFindColors import define_tiles
from groupTiles import grass_fire_algorithm

img = cv2.imread("./Cropped and perspective corrected boards/1.jpg")
templateCrown = cv2.imread('./Crown Images/crown4.jpg')
totalPoints = 0

#Separate Tiles into a list, going from 0-24
tiles = SeperatesTiles(img)
#print(tiles.__len__())

#Assign each tile its type
listOfAreas = define_tiles(tiles)
#print(listOfAreas)

#Create lists with each grouping of tiles
listOfGroups = grass_fire_algorithm(listOfAreas)
#print(listOfGroups)

#Find crowns in each grouping and calculate points
for group in listOfGroups:
    amountOfCrowns = find_crowns_in_group(group, tiles, templateCrown)
    totalPoints += amountOfCrowns * len(group)
    #print("group: ",group,"" " = Crowns: ", amountOfCrowns, "*", " Size: ",len(group)," = ", totalPoints)
print(totalPoints)
