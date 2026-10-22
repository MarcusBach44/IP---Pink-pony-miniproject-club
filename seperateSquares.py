
def SeperatesTiles(img):
    tiles = []

    rowDivision = 0
    height, width, channels = img.shape
    fifthHeight: int = height // 5
    fifthWidth: int = width // 5

    for row in range(5):
        rowDivision = rowDivision + fifthHeight
        columnDivision = 0

        for column in range(5):
            columnDivision = columnDivision + fifthWidth
            tile = img[rowDivision - fifthHeight:rowDivision , columnDivision - fifthWidth:columnDivision]
            tiles.append(tile)

    return tiles