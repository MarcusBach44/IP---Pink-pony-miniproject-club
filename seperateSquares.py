
def SeperatesTiles(img):
    tiles = []

    rowDivision = 0

    #Get the dimensions of the game board
    height, width, channels = img.shape

    #divide the image/board into 5 on both the rows and the colomns
    fifthHeight: int = height // 5
    fifthWidth: int = width // 5

    #Now in a for-loop, divide up the board into tiles
    for row in range(5):
        rowDivision = rowDivision + fifthHeight
        columnDivision = 0

        for column in range(5):
            columnDivision = columnDivision + fifthWidth
            tile = img[rowDivision - fifthHeight:rowDivision , columnDivision - fifthWidth:columnDivision]
            tiles.append(tile)

    #Return the list of tiles
    return tiles