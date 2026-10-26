

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