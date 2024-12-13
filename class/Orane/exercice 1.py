#Exercice 1
import pymel.core as pm

locators = pm.ls('locator*', type='transform')
def replace_cubes():
    for loc in locators:
        qube_trans, node = pm.polyCube()
        loc_trans = loc.getTranslation()
        pm.move(qube_trans, loc_trans, moveXYZ=True)
        pm.delete(loc)

replace_cubes()