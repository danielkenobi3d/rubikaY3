1.
import pymel.core as pm
locator_list = pm.ls('locator*',type='transform')
Cube= pm.polyCube()

for each in locator_list:
    transform, creation_node = pm.polyCube()
    pm.matchtransform(transform,each)
    print(each)

2.
import pymel.core as pm
import random

def rand_object():
    for each in range(10):
        Cube, create = pm.polyCube()
        pm.move(Cube, random.randrange(20, 30), random.randrange(20, 30), moveXYZ=True, relative=True, objectSpace=True)

rand_object()

3.
import pymel.core as pm

def cube_triangle():
    cube_size = 1
    spacing = 2
    num_rows = 5
    for row in range(num_rows):
        start_x = spacing
        for col in range (row + 1):
            x_pos = start_x + col * spacing
            y_pos = row * spacing
            z_pos = 0

            cube = pm.polyCube(w=cube_size, h=cube_size, d=cube_size)[0]
            pm.move(x_pos, y_pos, z_pos)

cube_triangle()

def cube_triangle1():
    cube_size = 1
    spacing = 2
    num_rows = 5
    for row in range(num_rows):
        start_x = 1 + spacing * num_rows * 2
        for col in range (row + 1):
            x_pos = start_x + col * -spacing
            y_pos = row * spacing
            z_pos = 0

            cube = pm.polyCube(w=cube_size, h=cube_size, d=cube_size)[0]
            pm.move(x_pos, y_pos, z_pos)

cube_triangle1()

def cube_trianglemirror():
    cube_size = 1
    spacing = 2
    num_rows = 5
    for row in range(num_rows):
        start_x = spacing
        start_y = -3
        for col in range (row + 1):
            x_pos = start_x + col * spacing
            y_pos = start_y + row * -spacing
            z_pos = 0

            cube = pm.polyCube(w=cube_size, h=cube_size, d=cube_size)[0]
            pm.move(x_pos, y_pos, z_pos)

cube_trianglemirror()

def cube_trianglemirror2():
    cube_size = 1
    spacing = 2
    num_rows = 5
    for row in range(num_rows):
        start_x = 1 + spacing *  num_rows * 2
        start_y = -3
        for col in range (row + 1):
            x_pos = start_x + col * -spacing
            y_pos = start_y + row * -spacing
            z_pos = 0

            cube = pm.polyCube(w=cube_size, h=cube_size, d=cube_size)[0]
            pm.move(x_pos, y_pos, z_pos)

cube_trianglemirror2()