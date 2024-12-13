import pymel.core as pm


def pyramid(size, positionX=0, positionY=0):
    for y in range(size):
        for x in range(size - y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, (x + 2) + positionX, (y - 2) + positionY, 0, moveXYZ=True)


def pyramid2(size, positionX=8, positionY=8):
    for y in range(size):
        for x in range(size - y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, (-x + 2) + positionX, (-y - 2) + positionY, 0, moveXYZ=True)


def pyramid3(size, positionX=0, positionY=8):
    for y in range(size):
        for x in range(size - y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, (x + 2) + positionX, (-y - 2) + positionY, 0, moveXYZ=True)


def pyramid4(size, positionX=8, positionY=0):
    for y in range(size):
        for x in range(size - y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, (-x + 2) + positionX, (y - 2) + positionY, 0, moveXYZ=True)


pyramid(4)
pyramid2(4)
pyramid3(4)
pyramid4(4)