import pymel.core as pm
import random

for each in range(20):
    x_value = random.randrange(0, 20)
    y_value = random.randrange(0, 20)
    z_value = random.randrange(0, 20)

    transform, creation_node = pm.polyCube()

    pm.move(transform, x_value, y_value, z_value, moveXYZ=True)