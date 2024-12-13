import pymel.core as pm

def create_cube():
    locator = pm.ls('locator*', type='transform')

    if not locator:
        print("Please place locator.")
        return

    for locator in locator:
        cube = pm.polyCube(name=f"{locator}_cube")[0]

        pm.matchTransform(cube, locator)

        pm.delete(locator)

create_cube()