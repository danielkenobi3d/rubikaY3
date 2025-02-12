from RMPY.rig import rigSingleJoint



def custom_rig():
    cylindreballefront_rig = rigSingleJoint.RigSingleJoint()
    cylindreballefront_rig.create_point_base('C_cylindreballefront00_reference_pnt',centered=True)

    pivotcylindreballefront_rig = rigSingleJoint.RigSingleJoint()
    pivotcylindreballefront_rig.create_point_base('C_pivotcylindreballefront00_reference_pnt', centered=True)

    marteau_rig = rigSingleJoint.RigSingleJoint()
    marteau_rig.create_point_base('C_marteau00_reference_pnt',centered=True)

    gachette_rig = rigSingleJoint.RigSingleJoint()
    gachette_rig.create_point_base('C_gachette00_reference_pnt',centered=True)

    handle_rig = rigSingleJoint.RigSingleJoint()
    handle_rig.create_point_base('C_handle00_reference_pnt',centered=True)