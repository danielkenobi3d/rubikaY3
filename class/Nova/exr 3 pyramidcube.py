import pymel.core as pm


def pyramid(size):
    for each_y in range(size):
        for each_x in range(size - each_y):
            transform, creation_node = pm.polyCube()
            pm.move(transform, each_x + 2, each_y - 2, 0, moveXYZ=True)


pyramid(6)