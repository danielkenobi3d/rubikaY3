import pymel.core as pm

def replace_cube():
    locators = pm.ls('locator*',type='transform')
    for locator in locators:
        cube = pm.polyCube()
        pm.matchTransform(cube,locator)
        pm.delete(locator)
rep_cube()
