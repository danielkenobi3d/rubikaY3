import pymel.core as pm

def create_joint_chain(locators, joint_grp):

    joints = []
    prev_joint = None

    for loc in locators:
        position = loc.getTranslation(space='world')
        joint = pm.joint(position=position, name=f"Joint_{loc}")
        joints.append(joint)

        if not prev_joint:
            pm.parent(joint, joint_grp)

        prev_joint = joint

    return joints

def create_controls(joints, control_grp):
    controls = []
    prev_ctrl = None

    for joint in joints:
        ctrl, _ = pm.circle(name=f"Ctrl_{joint}")
        pm.matchTransform(ctrl, joint)
        controls.append(ctrl)
        pm.parentConstraint(ctrl, joint, mo=True)

        if not prev_ctrl:
            pm.parent(ctrl, control_grp)
        else:
            pm.parent(ctrl, prev_ctrl)

        prev_ctrl = ctrl

    return controls


def fk_rig():

    locators = pm.ls('locator*', type='transform')

    joint_grp = pm.group(empty=True, name='Joint_Group')
    control_grp = pm.group(empty=True, name='Control_Group')

    joints = create_joint_chain(locators, joint_grp)
    create_controls(joints, control_grp)

    pm.delete('locator*')

fk_rig()
