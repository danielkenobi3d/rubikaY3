import pymel.core as pm


def FK_rig():
    locator_list = pm.ls(selection=True)
    jnt_list = []
    control_list = []

    jnt_group = pm.group(empty=True, name='Joints_group')

    for locator in locator_list:
        new_joint = pm.joint(name='joint' + locator)
        pm.matchTransform(new_joint, locator)
        jnt_list.append(new_joint)
        pm.delete(locator)

    for joints in jnt_list:
        new_control = pm.circle()
        pm.matchTransform(new_control, joints)
        control_list.append(new_control)
        pm.parentConstraint(new_control, joints, mo=True)

    control_group = pm.group('nurbsCircle*', name='Control_group')

FK_rig()