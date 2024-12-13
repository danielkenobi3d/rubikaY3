#Exercice 1
import pymel.core as pm

locators = pm.ls('locator*', type='transform')

for loc in locators:
    qube_trans, node = pm.polyCube()
    loc_trans = loc.getTranslation()
    pm.move(qube_trans, loc_trans, moveXYZ=True)
    pm.delete(loc)

#Exercice 2
import pymel.core as pm
import random

nb_cube = 20
position_max = 10
for i in range(0, nb_cube):
    x = random.randrange(-position_max, position_max)
    y = random.randrange(-position_max, position_max)
    z = random.randrange(-position_max, position_max)
    cube_trans, node = pm.polyCube()
    pm.move(cube_trans, x, y, z, moveXYZ=True)

#Exercice 3
import pymel.core as pm

def triangle(size, positionX=0, positionY=0, spacing=0.5):
    for i in range(0, size):
        for j in range(0, i + 1):
                cube, node = pm.polyCube()
                pm.move(cube, positionX + j * (1 + spacing), positionY + i * (1 + spacing), 0, moveXYZ=True)

triangle(10)