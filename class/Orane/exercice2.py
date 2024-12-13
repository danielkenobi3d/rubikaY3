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