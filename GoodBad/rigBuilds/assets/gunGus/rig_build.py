def custom_rig():
    pass

from RMPY.rig import rigSingleJoint
rig_barrel = rigSingleJoint.RigSingleJoint()
rig_barrel.creature_point_base('C_barrel00_refenrence_pnt',centered=True)

rig_trigger = rigSingleJoint.RigSingleJoint()
rig_trigger.creature_point_base('C_trigger00_refenrence_pnt',centered=True)

rig_hammer = rigSingleJoint.RigSingleJoint()
rig_hammer.creature_point_base('C_hammer00_refenrence_pnt',centered=True)

rig_handle = rigSingleJoint.RigSingleJoint()
rig_handle.creature_point_base('C_handle00_refenrence_pnt',centered=True)