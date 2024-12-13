import pymel.core as pm


def FK_rig():
    locator_list = pm.ls('locatorShape*')
    jnt_list = []
    control_list = []
    print(locator_list)

    locator_list.sort(key=lambda locator: locator.getParent().getTranslation(space='world').x)

    jnt_group = pm.group(empty=True, name='Joints_group')

    for locator in locator_list:
        joint_name = 'joints' + 'locator*'
        new_joint = pm.joint(name=joint_name)
        pm.matchTransform(new_joint, locator)
        jnt_list.append(new_joint)

    control_group = pm.group(empty=True, name='Control_group')

    for joints in jnt_list:
        control_name = 'ctrl_' + 'joints*'
        new_control = pm.circle(name=control_name)
        pm.matchTransform(new_control, joints)
        control_list.append(new_control)
        pm.parent(new_control, control_group)
        pm.parentConstraint(new_control, joints)


FK_rig()