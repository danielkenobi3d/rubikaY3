import pymel.core as pm


def triangle_1():
    for i in range(5):
        for j in range(i + 1):
            cube = pm.polyCube(w=1, h=1, d=1)
            x = j * 2
            y = i * 2
            pm.move(x, y, 0)



def triangle_2():
    for i in range(5):
        for j in range(i + 1):
            cube = pm.polyCube(w=1, h=1, d=1)
            x = i * 2
            y = j * 2
            pm.move(x, y, 0)


def triangle_3 () :
    for i in range (5) :
       for j in range (i+1) :
        cube = pm.polyCube(w=1, h=1, d=1)
        x = i * 2
        y = j * 2
        pm.move(-x, y, 0)


def triangle_4():
    for i in range(5):
        for j in range(i + 1):
            cube = pm.polyCube(w=1, h=1, d=1)
            x = j * 2
            y = i * 2
            pm.move(-x, y, 0)
