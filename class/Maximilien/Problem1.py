import pymel.core as pm

list_of_locators = pm.ls('locator*', type ='transform')

for each in pm.ls('locator*', type ='transform'):
    print(each)


for each in list_of_locators :
    cube1, create_node = pm.polyCube()
    pm.matchTransform(cube1,each,position=True,rotation=True,scale=True)
