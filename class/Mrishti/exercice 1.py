import pymel.core as pm

# list_of_objects = pm.ls('name_token * ', objectType='transform')
list = pm.ls('locator*', type='transform')

for each_locator in list:
    transform, creation_node = pm.polyCube()

    # pm.matchTransforms(source, destination)
    pm.matchTransform(transform, each_locator)