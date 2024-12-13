import pymel.core as pm

list_of_locator = pm.ls(selection=True)

for each in list_of_locator:
    transform, creation_node = pm.polyCube()
    pm.matchTransform(transform, each)

