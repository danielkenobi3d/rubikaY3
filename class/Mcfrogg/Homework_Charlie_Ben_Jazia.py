1.

import pymel.core as pm
locator_list = pm.ls('locator*',type='transform')
sphere= pm.polySphere()

for each in locator_list:
    transform, creation_node = pm.polySphere()
    pm.matchTransform(transform,each)
    print(each)

2.

import pymel.core as pm
import random

def rand_object():
    for each in range(5):
        Sphere, creat = pm.polySphere()
        pm.move(Sphere,random.randrange(1,5),random.randrange(1,5),random.randrange(1,5),moveXYZ=True,relative=True,objectSpace=True)

rand_object()


3.

import pymel.core as pm


def triangle_wall():
    cube_size = 2
    spacing = 4
    row = 6
    for row in range(row):
        x_position = spacing
        for col in range(row + 1):
            x_pos = x_position + col * spacing
            y_pos = row * spacing
            z_pos = 0

            cube = pm.polyCube(w=cube_size, h=cube_size, d=cube_size)[0]
            pm.move(x_pos, y_pos, z_pos)


triangle_wall()

