import pymel.core as pm

def locators_to_cubes():
    locators = pm.ls('locator*', type='transform')

    for locator in locators:
        cube = pm.polyCube(name=f"{locator}_cube")[0]

        pm.matchTransform(cube, locator)

        pm.delete(locator)

locators_to_cubes()





import pymel.core as pm

from random import random, randrange


def random_cube():
    random_number = randrange(1, 50)
    for each in range(random_number):
        cube = pm.polyCube()[0]
        pm.move(cube, random()*50, random()*50, random()*50, moveXYZ=True)


random_cube()



import pymel.core as pm

def cube_staircase (n):
    for i in range(n):
        for j in range(i + 1):
            x = i * 2
            y = j * 2
            z = 0

            mirrored_x = -x

            cube = pm.polyCube(w=1, h=1, d=1)[0]
            pm.move(mirrored_x, y, z)

cube_staircase (8)