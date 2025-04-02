import pymel.core as pm
def create_animation_points():
    selection  = pm.ls(selection=True)
    if selection:
        namespace=selection[0].split(':')[0]

        side = 'R'

        arm_controls = pm.ls(f'{namespace}:{side}_ikPoleVectorIK00_arm_ctr', f'{namespace}:{side}_ikIK00_arm_ctr',
                        f'{namespace}:{side}_fk00_arm_ctr', f'{namespace}:{side}_fk01_arm_ctr')


        start_time = pm.playbackOptions(q=True, minTime=True)
        end_time = pm.playbackOptions(q=True, maxTime=True)
        original_time = pm.currentTime(q=True)
        # constraint_list=[]
        space_locators_list=[]
        new_group = pm.group(name='anim_locators', empty=True)
        new_group.scaleZ.set(-1)
        for each_control in arm_controls:
            new_space_locator = pm.spaceLocator(name=each_control.replace('_ctr','_pnt'))
            # constraint_list.append(pm.parentConstraint(each_control, new_space_locator))
            space_locators_list.append(new_space_locator)
            new_space_locator.setParent(new_group)

        for frame in range(int(start_time), int(end_time + 1)):
            pm.currentTime(frame, e=True)
            for each_space_locator, each_control in zip(space_locators_list, arm_controls):
                pm.matchTransform(each_space_locator, each_control)
                for axis in 'XYZ':
                    pm.setKeyframe(each_space_locator.attr(f'translate{axis}'))
                    pm.setKeyframe(each_space_locator.attr(f'rotate{axis}'))
        # pm.delete(constraint_list)
    else:
        print('select a an object of the rig to bake')
create_animation_points()

