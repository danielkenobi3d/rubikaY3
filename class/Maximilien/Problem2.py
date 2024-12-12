import pymel.core as pm
import random
print(random.random())


for each in range(10):
    cube, shape = pm.polyCube()
    x_value = random.randrange(-10,10)
    y_value = random.randrange(-10,10)
    z_value = random.randrange(-10,10)
    x_rotate = random.randrange(0,360)
    y_rotate = random.randrange(0,360)
    z_rotate = random.randrange(0,360)
    pm.move(cube, x_value, y_value, z_value, moveXYZ=True, relative=True)
    pm.rotate(cube, x_rotate, y_rotate, z_rotate, rotateXYZ=True, relative=True)