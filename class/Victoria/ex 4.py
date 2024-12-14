import pymel.core as pm
list_of_locator = pm.ls(selection=True)
list_of_joint = []
list_of_controller = []

    list_of_joint = pm.group(empty=True, name='Joints_group')

    for locator in list_of_locator:

        new_joint= pm.joint(name= 'joint'+locator)
        pm.matchTransform(new_joint,locator)
        list_of_joint.append(new_joint)
        pm.delete(locator)

    for joints in list_of_joint:
        new_control = pm.circle()
        pm.matchTransform(new_control,joints)
        list_of_controller.append(new_control)
        pm.parentConstraint(new_control,joints, mo=True)

    control_group= pm.group('nurbsCircle*', name='Control_group'