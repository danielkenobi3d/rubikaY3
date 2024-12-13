import pymel.core as pm
import random


def rand_object():
    for each in range(10):
        Cube, creat = pm.polyCube()
        pm.move(Cube, random.randrange(1, 10), random.randrange(1, 10), random.randrange(1, 10), moveXYZ=True,
                relative=True, objectSpace=True)


rand_object()
