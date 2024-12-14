import pymel.core as pm
def FK_rig():
    locator_list = pm.ls(selection=True)
    jnt_list = []
    control_list = []
    jnt_group = pm.group(empty=True, name='Joints_group')
    for locator in locator_list:
        new_joint = pm.joint(name=f'joint_{locator}')
        pm.matchTransform(new_joint, locator)
        jnt_list.append(new_joint)
        pm.parent(new_joint, jnt_group)
        pm.delete(locator)

    for joint in jnt_list:
        new_control, _ = pm.circle(name=f'control_{joint}')
        pm.matchTransform(new_control, joint)
        control_list.append(new_control)
        pm.parentConstraint(new_control, joint, mo=True)

    control_group = pm.group(control_list, name='Control_group')
FK_rig()