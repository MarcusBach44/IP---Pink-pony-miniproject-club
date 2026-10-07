import numpy as np

"""Vi skal have sat noget op til at vurdere hvor mange spilleplader vi har og dermed hvor mange spillere vi har"""
players = [1, 2, 3, 4]

"""#Here is where we should put the generalised colors of the squares - i just chose red, green and blue as a start
red = np.array([255, 0, 0])
green = np.array([0, 255, 0])
blue = np.array([0, 0, 255])

#Here are the square types
forestSquare = []
waterSquare = []
fieldSquare = []
mineSquare = []
hillSquare = []
desertSquare = []

def squareColor():
    return np.array([red, green, blue])

def square():
    if squareColor():
        return"""