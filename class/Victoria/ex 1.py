import pymel.core as pm
list_of_locators = pm.ls('locator * ', type='transform')
for locator in list_of_locators :
    transform, creation_node = pm.polyCube()
     pm.matchTransform(transform,locator)