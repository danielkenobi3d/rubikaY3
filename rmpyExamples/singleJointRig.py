
from RMPY.rig import rigSingleJoint

blade_rig = rigSingleJoint.RigSingleJoint()
blade_rig.create_point_base('C_blade00_reference_pnt')

shoe_rig = rigSingleJoint.RigSingleJoint()
shoe_rig.create_point_base('L_shoe00_reference_pnt')

