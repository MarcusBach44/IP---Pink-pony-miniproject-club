

def find_surrounding_tiles(currentTileIndex, tiles):
    positionsOfSurroundingTiles = [currentTileIndex]

    if currentTileIndex > 4:
        positionsOfSurroundingTiles.append(currentTileIndex -5)
    if not currentTileIndex % 5 == 0:
        positionsOfSurroundingTiles.append(currentTileIndex - 1)
    if not currentTileIndex % 5 == 4:
        positionsOfSurroundingTiles.append(currentTileIndex + 1)
    if currentTileIndex < len(tiles) - 5:
        positionsOfSurroundingTiles.append(currentTileIndex + 5)

    return positionsOfSurroundingTiles


def addToBurnQueue(burnQueue, currentTileIndex, tiles, burnedTiles):
    indexOfSurroundingTiles = find_surrounding_tiles(currentTileIndex, tiles)
    for tileIndex in indexOfSurroundingTiles:
        if tiles[currentTileIndex] == tiles[tileIndex] and tileIndex not in burnedTiles and tileIndex not in burnQueue:
            burnQueue.append(tileIndex)
    return burnQueue

def burnTiles(tiles, currentTileIndex, burnedTiles):
    currentGroup = []

    burnQueue = []

    #burnQueue.append(currentTileIndex)
    currentGroup = burnTile(burnQueue, currentTileIndex, tiles, burnedTiles, currentGroup)

    return currentGroup, burnedTiles


def burnTile(burnQueue, currentTileIndex, tiles, burnedTiles, currentGroup):
    burnQueue = addToBurnQueue(burnQueue, currentTileIndex, tiles, burnedTiles)
    for tileIndex in burnQueue:
        burnedTiles.append(tileIndex)
        currentGroup.append(tileIndex)
        burnQueue.remove(tileIndex)
        burnTile(burnQueue, tileIndex, tiles, burnedTiles, currentGroup)
    return currentGroup



def grass_fire_algorithm(tiles):
    ListOfGroups = []
    burnedTiles = []

    for currentTileIndex in range(len(tiles)):
        #Add matching tiles to burnQueue
        currentGroup, burnedTiles = burnTiles(tiles, currentTileIndex, burnedTiles)
        if not currentGroup == []:
            ListOfGroups.append(currentGroup)

    return ListOfGroups




"""def check_surrounding_tiles(currentTileIndex, tiles, ListOfGroups):
    listOfSurroundingTiles = find_surrounding_tiles(currentTileIndex, tiles)
    currentGroup = []
    currentGroup.append(tiles[currentTileIndex])
    for tile in listOfSurroundingTiles:
        if tile == tiles[currentTileIndex] and not currentGroup.contains(tile):
            isInGroup, group = is_already_grouped(tile, ListOfGroups)
            if isInGroup:
                group.append(tiles[currentTileIndex])
                currentGroup.remove(tiles[currentTileIndex])
            else:
                currentGroup.append(tile)
                
    def is_already_group(tile, ListOfGroups):
    for group in ListOfGroups:
        if group.contains(tile):
            return True, group
    return False, None"""


##########################################################
"""
def possibleTiles():
    listOfAreas = ["water ", "mine ", "field ", "forrest ", "plain ", "desert "]
    listOfTilePos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    listOfPossibleTiles = []

    for area in listOfAreas:
        for tilePos in listOfTilePos:
            listOfPossibleTiles.append(area + str(tilePos))
    return listOfPossibleTiles

def CheckNeighbors(tileNumber, tileArray, currTile, currTileNumber):
    behindNum = tileNumber - 1
    aboveNum = tileNumber - 5

    behindTile = color.check_color(tileArray[behindNum])
    aboveTile = color.check_color(tileArray[aboveNum])

    behindGathered = behindTile + str(behindNum)
    aboveGathered = aboveTile + str(aboveNum)

    newList = []

    if behindNum > 0 and behindTile == currTile and aboveNum > 0 and aboveTile == currTile:
        newList = list([currTileNumber, behindGathered, aboveGathered])

    else:
        if behindNum > 0 and behindTile == currTile:
            newList = list([currTileNumber, behindGathered])

        if aboveNum > 0 and aboveTile == currTile:
            newList = list([currTileNumber, aboveGathered])

    return newList

##########################################################

def ThroughTiles(listOfLists):
    tile = ""
    for list in listOfLists:
        for tile in list:
            return tile
        return tile
    return tile


def NewCheck(listOfLists):
    for list in listOfLists:
        for tile in list:
            result = [tile for tile in list if tile in b]

            return
        return
    return





def TroughLists(listOfLists):
    tile = ""
    for list in listOfLists:
        return list
    return list


def joinLists(listOfList):
            for PossTile in possibleTiles():
            any(x == 30 for list in listOfLists)

        if list == PossTile:
            print("X")
    
    
    
    tileNumbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    togetherLists = []
    num = 0

    for list in listOfList:
        currList = listOfList[len(listOfList[num])]

        for nr in tileNumbers:
            if str(nr) in currList:
                newList = list[nr] + currList
                togetherLists.append(newList)

        num = num + 1
    return togetherLists


def checkLists(listOfList):
    item = ""
    for list in listOfList:
        listLength = len(list)
        otherCurrList = listOfList[listLength]

        for item in otherCurrList:
            return item
        return item
    return item"""