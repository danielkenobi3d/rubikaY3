import pymel.core as pm
from random import random, randrange

def random_objects():

    number_of_cubes = randrange(0,10)

    for each in range(number_of_cubes):
        cube = pm.polyCube[0]
        pm.move(cube, random()*10, random()*10, random()*10, moveXYZ=True)
