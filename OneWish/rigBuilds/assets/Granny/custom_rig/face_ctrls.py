import pymel.core as pm
from RMPY.rig import rigSingleJoint
from RMPY.rig import rigStaticLayer
from RMPY.core import data_save_load
from RMPY.rig import rigLaces

def build():
    R_static_lowerLid_root = pm.ls('R_Lower_Lid_reference_points')[0]
    R_static_lowerLid_layers = rigStaticLayer.StaticLayer('body','reyelash', name='RstaticeLowerLid')
    R_static_lowerLid_rig = rigSingleJoint.RigSingleJoint()
    R_static_lowerLid_rig.create_point_base(*R_static_lowerLid_root.getChildren(), static=True)
    R_static_lowerLid_rig.zero_joint
    R_static_lowerLid_rig.set_parent(pm.ls('C_fk00_head_ctr')[0])


    data_save_load.load_skin_cluster(*R_static_lowerLid_layers.static_geometries)

    L_static_lowerLid_root = pm.ls('L_Lower_Lid_reference_points')[0]
    L_static_lowerLid_layers = rigStaticLayer.StaticLayer('body','reyelash', name='LstaticeLowerLid')
    L_static_lowerLid_rig = rigSingleJoint.RigSingleJoint()
    L_static_lowerLid_rig.create_point_base(*L_static_lowerLid_root.getChildren(), static=True)
    L_static_lowerLid_rig.zero_joint
    L_static_lowerLid_rig.set_parent(pm.ls('C_fk00_head_ctr')[0])


    data_save_load.load_skin_cluster(*L_static_lowerLid_layers.static_geometries)
