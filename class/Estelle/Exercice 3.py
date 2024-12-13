#1

import pymel.core as pm

def staircase_3d(n):
    for i in range(n):
        for j in range(i + 1):
            x = j * 2
            y = i * 2
            z = 0

            cube = pm.polyCube(w=1, h=1, d=1)[0]
            pm.move(x, y, z)


staircase_3d(5)

#2

import pymel.core as pm

def staircase_3d_rotated(n):
    for i in range(n):
        for j in range(i + 1):
            x = i * 2
            y = j * 2
            z = 0

            cube = pm.polyCube(w=1, h=1, d=1)[0]
            pm.move(x, y, z)


staircase_3d_rotated(5)

#3

import pymel.core as pm

def staircase_3d_rotated_mirrored(n):
    for i in range(n):
        for j in range(i + 1):
            x = i * 2
            y = j * 2
            z = 0

            mirrored_x = -x

            cube = pm.polyCube(w=1, h=1, d=1)[0]
            pm.move(mirrored_x, y, z)


staircase_3d_rotated_mirrored(5)

#4

import pymel.core as pm

def staircase_3d_mirrored(n):
    for i in range(n):
        for j in range(i + 1):
            x = j * 2
            y = i * 2
            z = 0

            cube = pm.polyCube(w=1, h=1, d=1)[0]
            pm.move(x, y, z)

            mirrored_x = -x
            pm.move(mirrored_x, y, z)


staircase_3d_mirrored(5)