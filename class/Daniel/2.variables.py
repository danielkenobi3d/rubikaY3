import pymel.core as pm

for each in pm.ls('locator*', type='transform'):
    print(each)

list_of_object = pm.ls('locator*', type='transform'):
cube1, create_node = pm.polyCube()
cube2, create_node = pm.polyCube()

for each in list_of_object :
    pm.matchTransforms(cube1, list_of_object)
    pm.matchTransforms(cube2, list_of_object)

