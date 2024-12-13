import pymel.core as pm

cube = 5
for index_y in range(cube):
    for index_z in range(index_y + 1):
        for index_x in range(index_y + 1):
            transform, pcube = pm.polyCube()
            pcube.width.set(.8)
            pcube.height.set(.8)
            pcube.depth.set(.8)
            transform.translateY.set(1 + index_y)
            transform.translateX.set(index_x)

cube = 5
for index_y in range(cube):
    for index_z in range(index_y + 1):
        for index_x in range(index_y + 1):
            transform, pcube = pm.polyCube()
            pcube.width.set(.8)
            pcube.height.set(.8)
            pcube.depth.set(.8)
            transform.translateY.set(-1 - index_y)
            transform.translateX.set(index_x)

cube = 5
for index_y in range(cube):
    for index_z in range(index_y + 1):
        for index_x in range(index_y + 1):
            transform, pcube = pm.polyCube()
            pcube.width.set(.8)
            pcube.height.set(.8)
            pcube.depth.set(.8)
            transform.translateY.set(-1 - index_y)
            transform.translateX.set(10.5 - index_x)

cube = 5
for index_y in range(cube):
    for index_z in range(index_y + 1):
        for index_x in range(index_y + 1):
            transform, pcube = pm.polyCube()
            pcube.width.set(.8)
            pcube.height.set(.8)
            pcube.depth.set(.8)
            transform.translateY.set(1 + index_y)
            transform.translateX.set(10.5 - index_x)