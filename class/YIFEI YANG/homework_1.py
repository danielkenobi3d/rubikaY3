import pymel.core as pm

def replace_locators_with_cubes():
    locators = pm.ls('locator*',type='transform')
    for locator in locators:
        cube = pm.polyCube()
        pm.matchTransform(cube,locator)
        pm.delete(locator)
replace_locators_with_cubes()
