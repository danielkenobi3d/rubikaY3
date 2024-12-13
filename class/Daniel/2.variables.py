<<<<<<< HEAD
+import pymel.core as pm
cube_return = pm.polyCube()
print(cube_return)
cube_transform = cube_return[0]
creation_cube = cube_return[1]
creation_cube.depth.set(10)
creation_cube.height.set(5)
creation_cube.width.set(5)
creation_cube.subdivisionsDepth.set(10)
creation_cube.depth.set(creation_cube.depth.get()+2)
=======
import pymel.core as pm

for each in pm.ls('locator*', type='transform'):
    print(each)

list_of_object = pm.ls('locator*', type='transform'):
cube1, create_node = pm.polyCube()
cube2, create_node = pm.polyCube()

for each in list_of_object :
    pm.matchTransforms(cube1, list_of_object)
    pm.matchTransforms(cube2, list_of_object)

>>>>>>> b69564bf2da018fb594b10e63961dc27937d6a1c
