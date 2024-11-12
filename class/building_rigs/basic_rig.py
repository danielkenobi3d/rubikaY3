from RMPY.rig import rigSingleJoint
from RMPY.rig import rigFK
import pymel.core as pm


selection = pm.ls(selection=True)
# rig_joint = rigSingleJoint.RigSingleJoint()
rig_joint = rigFK.RigFK()
rig_joint.create_point_base(*selection)