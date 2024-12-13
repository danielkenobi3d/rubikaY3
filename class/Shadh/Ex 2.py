import pymel.core as pm
import random


def rand_object():
    for each in range(10):
        cube, creat = pm.polyCube()
        pm.move(cube, random.randrange(1, 20), random.randrange(1, 20), random.randrange(1, 20), moveXYZ=True,
                relative=True, objectSpace=True)


rand_object()