import random
import pymel.core as pm


def random_object():

    for each in range(20):
        cube, creat = pm.polyCube()
        pm.move(cube, random.randrange(1,30) , random.randrange(1,30), random.randrange(1,30) , moveXYZ=True, relative=True, objectSpace=True)

random_object()