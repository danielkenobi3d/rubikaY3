computer = 5
apple = 3.4
keyboard='my number '
mouse = "45"
result =  keyboard + str(computer)
print(result, type(result))


import pymel.core as pm
cube_return = pm.polyCube()
print (cube_return)
cube_transform = cube_return[0]
creation_cube = cube_return[1]
creation_cube.depth.set(10)
creation_cube.height.set(5)
creation_cube.width.set(5)
creation_cube.subdivisionsDepth.set(10)
creation_cube.depth.set(creation_cube.depth.get(10)+2)