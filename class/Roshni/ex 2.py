from random import random

import pymel.core as pm

def rand_object():
    for each in range(10):
        cube, creat = pm.polyCube()
        pm.move(cube, random.randrange(1, 10), random.randrange(1, 10), random.randrange(1, 10), moveXYZ=True,
                relative=True, objectSpace=True)


rand_object()