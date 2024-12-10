import pymel.core as pm

def replace_locators_with_cubes():
    #finding the locators
    locators = pm.ls('locator*', type='transform')

    if not locators:
        print("No locators found in the scene.")
        return

    for locator in locators:
        # getting attributes from each locators
        position = locator.getTranslation(space='world')
        rotation = locator.getRotation(space='world')
        scale = locator.getScale()

        # cube
        cube = pm.polyCube(name=f"{locator}_cube")[0]

        # Match the locator's transform attributes
        cube.setTranslation(position, space='world')
        cube.setRotation(rotation, space='world')
        cube.setScale(scale)

        pm.delete(locator)

# Run the function
replace_locators_with_cubes()


import pymel.core as pm

def replace_locators_with_cubes():
    #finding the locators
    locators = pm.ls('locator*', type='transform')

    if not locators:
        print("No locators found in the scene.")
        return

    for locator in locators:
        # getting attributes from each locators

        # cube
        cube = pm.polyCube(name=f"{locator}_cube")[0]

        # Match the locator's transform attributes
        pm.matchTransform(cube, locator)

        pm.delete(locator)

# Run the function
replace_locators_with_cubes()