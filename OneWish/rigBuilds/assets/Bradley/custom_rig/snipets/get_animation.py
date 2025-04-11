import pymel.core as pm


def get_animation():
    selection = pm.ls(selection=True)
    if selection:
        namespace = selection[0].split(':')[0]

        side = 'R'

        arm_controls = pm.ls(f'{namespace}:{side}_ikPoleVectorIK00_arm_ctr', f'{namespace}:{side}_ikIK00_arm_ctr',)
                             # f'{namespace}:{side}_fk00_arm_ctr', f'{namespace}:{side}_fk01_arm_ctr')

        start_time = pm.playbackOptions(q=True, minTime=True)
        end_time = pm.playbackOptions(q=True, maxTime=True)
        original_time = pm.currentTime(q=True)
        locator_list= []
        for each_control in arm_controls:
            space_locator = each_control.replace('_ctr','_pnt')
            locator_list.append(space_locator)
            delete_animation(each_control)

        for frame in range(int(start_time), int(end_time + 1)):
            pm.currentTime(frame, e=True)
            for each_locator, each_control in zip(locator_list, arm_controls):
                pm.matchTransform(each_control, each_locator, position=True)
                for axis in 'XYZ':
                    pm.setKeyframe(each_control.attr(f'translate{axis}'))
                    # pm.setKeyframe(each_control.attr(f'rotate{axis}'))
        # pm.delete(locator_list)
    else:
        print('select a an object of the rig to bake')
def delete_animation(scene_object):
    pm.delete(pm.listConnections(scene_object, type='animCurveTL'))
    pm.delete(pm.listConnections(scene_object,type='animCurveTA'))
    pm.delete(pm.listConnections(scene_object,type='animCurveTU'))


get_animation()