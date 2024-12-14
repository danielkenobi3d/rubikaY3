import pymel.core as pm

list_of_objects = pm.ls('name_token * ', objectType='transform')

for each in list:
    transform, creation_node = pm.polyCube()

    pm.matchTransform(transform, each)