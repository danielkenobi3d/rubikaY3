import pymel.core as pm
import random
for each in range(50):
    transform, creation_node = pm.polyCube()
    x_number = random.randrange(-50, 50)
    y_number = random.randrange(-50, 50)
    z_number = random.randrange(-50, 50)
    pm.move(transform,x_number,y_number,z_number,moveXYZ=True)