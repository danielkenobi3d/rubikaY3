import pymel.core as pm

list_of_locator = pm.ls('locator*',type='transform')

for each in list_of_locator :
    print(each)
    transform, creation_node = pm.polyCube()
    pm.matchTransform(transform,each)
    print('pCube*')




import pymel.core as pm
import random

for each in range(10):
    x_value = random.randrange(0, 10)
    y_value = random.randrange(0, 10)
    z_value = random.randrange(0, 10)

    transform, creation_node = pm.polyCube()
    pm.move(transform, x_value, y_value, z_value, moveXYZ=True)
