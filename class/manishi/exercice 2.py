import pymel.core as pm
import random

def rand_object():

    for each in range(16):
        cube, creat = pm.polyCube()
        pm.move(cube, random.randrange(1,10) , random.randrange(1,15), random.randrange(1,15) , moveXYZ=True, relative=True, objectSpace=True)

rand_object()