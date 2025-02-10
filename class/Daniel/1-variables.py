computer = 5
apple = 3.4
keyboard='my number '
mouse = "45"
result =  keyboard + str(computer)
print(result, type(result))
<<<<<<< HEAD


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
=======
          # 0   1  2  3  4
my_list = [23,454,23.5, 'my_name',56]

print(my_list[3])
>>>>>>> eff030f8297632635f3f1ec9602375be61ff8ca4
