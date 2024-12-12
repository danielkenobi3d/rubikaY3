import pymel.core as pm

def put_cube_at(x, y):

    transform, creation_node = pm.polyCube()
    transform.translateX.set(x)
    transform.translateY.set(y)

def triangle_top_left(size):

    for i in range(size):
        for j in range(i + 1):
            put_cube_at(j, i)

def triangle_top_right(size):

    for i in range(size):
        for j in range(i + 1):
            put_cube_at(size - 1 - j, i)

def triangle_bottom_left(size):

    for i in range(size):
        for j in range(i + 1):
            put_cube_at(j, size - 1 - i)

def triangle_bottom_right(size):

    for i in range(size):
        for j in range(i + 1):
            put_cube_at(size - 1 - j, size - 1 - i)

triangle_bottom_left(size=5)


