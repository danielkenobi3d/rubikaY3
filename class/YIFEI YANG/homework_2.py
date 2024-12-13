import pymel.core as pm
import random
for each in range(15):
    transform,creation_node = pm.polyCube()
    x_value = random.randrange(0,10)
    y_value = random.randrange(0,10)
    z_value = random.randrange(0,10)
    pm.move(transform,x_value,y_value,z_value,moveXYZ=True)