import pymel.core as pm

def staircase_3d(n, spacing=2, mirror_x=1, mirror_y=1, mirror_z=1, offset_x=0, offset_y=0, offset_z=0):
    for i in range(n):
        for j in range(i + 1):

            x = (j * spacing + offset_x) * mirror_x
            y = (i * spacing + offset_y) * mirror_y
            z = (0 + offset_z) * mirror_z

            cube = pm.polyCube(w=1, h=1, d=1)[0]
            pm.move(x, y, z, cube)


staircase_3d(5, spacing=2, mirror_x=1, mirror_y=1, mirror_z=1, offset_x=0, offset_y=0)
staircase_3d(5, spacing=2, mirror_x=1, mirror_y=-1, mirror_z=1, offset_x=0, offset_y=2)
staircase_3d(5, spacing=2, mirror_x=-1, mirror_y=1, mirror_z=1, offset_x=-18, offset_y=0)
staircase_3d(5, spacing=2, mirror_x=-1, mirror_y=-1, mirror_z=1, offset_x=-18, offset_y=2)