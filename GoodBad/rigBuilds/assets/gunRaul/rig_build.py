from RMPY.rig import rigSingleJoint
from RMPY.rig import rigWorld


def custom_rig():
    cylindreballe_rig = rigSingleJoint.RigSingleJoint()
    cylindreballe_rig.create_point_base('C_cylindreballe00_reference_pnt',centered=True)

    pivotcylindreballe_rig = rigSingleJoint.RigSingleJoint()
    pivotcylindreballe_rig.create_point_base('C_pivotcylindreballe00_reference_pnt', centered=True)

    cylindreballe_rig.set_parent(pivotcylindreballe_rig)

    marteau_rig = rigSingleJoint.RigSingleJoint()
    marteau_rig.create_point_base('C_marteau00_reference_pnt',centered=True)

    gachette_rig = rigSingleJoint.RigSingleJoint()
    gachette_rig.create_point_base('C_gachette00_reference_pnt',centered=True)

    handle_rig = rigSingleJoint.RigSingleJoint()
    handle_rig.create_point_base('C_handle00_reference_pnt',centered=True)

    marteau_rig.set_parent(handle_rig)
    gachette_rig.set_parent(handle_rig)
    pivotcylindreballe_rig.set_parent(handle_rig)
    rig_world = rigWorld.RigWorld()
    handle_rig.set_parent(rig_world)