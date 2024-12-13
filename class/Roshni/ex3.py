import pymel.core as pm

def triangle1(n):
    for i in range(n):
        for j in range(i + 1):
            x = j * 2
            y = i * 2
            z = 0

            cube = pm.polyCube(w=1, h=1, d=1)
            pm.move(x, y, z)


import pymel.core as pm

def triangle1_rotated(n):
    for i in range(n):
        for j in range(i + 1):
            x = i * 2
            y = j * 2
            z = 0

            cube = pm.polyCube(w=1, h=1, d=1)
            pm.move(x, y, z)


import pymel.core as pm

def triangle1_rotated_mirrored(n):
    for i in range(n):
        for j in range(i + 1):
            x = i * 2
            y = j * 2
            z = 0

            mirrored_x = -x

            cube = pm.polyCube(w=1, h=1, d=1)
            pm.move(mirrored_x, y, z)


import pymel.core as pm

def triangle1_mirrored(n):
    for i in range(n):
        for j in range(i + 1):
            x = j * 2
            y = i * 2
            z = 0

            cube = pm.polyCube(w=1, h=1, d=1)
            pm.move(x, y, z)

            mirrored_x = -x
            pm.move(mirrored_x, y, z)
