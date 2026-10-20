import blurPicturesAndFindColors as color

##########################################################

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

def joinLists(listOfList):
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
    return item