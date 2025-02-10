import pymel.core as pm


def triangle(size, positionx=0, positiony=0):
    for y in range(size):
        for x in range(size - y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, (x + 2) + positionx, (y - 2) + positiony, 0, moveXYZ=True)


def triangle2(size, positionx=8, positiony=8):
    for y in range(size):
        for x in range(size - y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, (-x + 2) + positionx, (-y - 2) + positiony, 0, moveXYZ=True)


def triangle3(size, positionx=0, positiony=8):
    for y in range(size):
        for x in range(size - y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, (x + 2) + positionx, (-y - 2) + positiony, 0, moveXYZ=True)


def triangle4(size, positionx=8, positiony=0):
    for y in range(size):
        for x in range(size - y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, (-x + 2) + positionx, (y - 2) + positiony, 0, moveXYZ=True)


triangle(4)
triangle2(4)
triangle3(4)
triangle4(4)