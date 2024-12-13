import pymel.core as pm

selected_objects = pm.ls(selection=True)

list_of_objects = pm.ls('locator*', type='transform')

print (list_of_objects)

for locator in list_of_objects:
    print(locator, 'name_token*')