import pymel.core as pm
locator_list = pm.ls('locator*',type='transform')
Cube= pm.polyCube()

for each in locator_list:
    transform, creation_node = pm.polyCube()
    pm.matchTransform(transform,each)
    print(each)