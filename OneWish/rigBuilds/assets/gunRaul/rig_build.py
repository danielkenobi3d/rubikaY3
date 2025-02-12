from RMPY.rig import rigSingleJoint

def custom_rig():
    rig_barrel = rigSingleJoint.RigSingleJoint()
    rig_barrel.create_point_base('C_barrel00_reference_pnt', centered=True)

    rig_trigger = rigSingleJoint.RigSingleJoint()
    rig_trigger.create_point_base('C_trigger00_reference_pnt', centered=True)

    rig_hammer = rigSingleJoint.RigSingleJoint()
    rig_hammer.create_point_base('C_hammer00_reference_pnt', centered=True)

    rig_handle = rigSingleJoint.RigSingleJoint()
    rig_handle.create_point_base('C_handle00_reference_pnt', centered=True)

    rig_barrel.set_parent(rig_handle)
    rig_trigger.set_parent(rig_handle)
    rig_hammer.set_parent(rig_handle)