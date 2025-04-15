import pymel.core as pm
from RMPY.rig import rigSingleJoint
from RMPY.rig import rigStaticLayer
from RMPY.core import data_save_load
from RMPY.rig import rigLaces

def build():
     #L_static_ebrows_root = pm.ls('L_eyebrows_reference_points')[0]
    L_static_ebrows_layers = rigStaticLayer.StaticLayer('main','eyebrows', name='Lstaticebrows')
    L_static_ebrows_rig = rigSingleJoint.RigSingleJoint()
    L_static_ebrows_rig.create_point_base('L_staticeyebrow00_reference_pnt','L_staticeyebrow01_reference_pnt','L_staticeyebrow02_reference_pnt','L_staticeyebrow03_reference_pnt','L_staticeyebrow04_reference_pnt', static=True)
    L_static_ebrows_rig.zero_joint
    L_static_ebrows_rig.set_parent(pm.ls('C_fk00_head_ctr')[0])


    data_save_load.load_skin_cluster(*L_static_ebrows_layers.static_geometries)

    R_static_ebrows_root = pm.ls('R_eyebrows_reference_points')[0]
    R_static_ebrows_layers = rigStaticLayer.StaticLayer('main','eyebrows', name='Rstaticebrows')
    R_static_ebrows_rig = rigSingleJoint.RigSingleJoint()
    R_static_ebrows_rig.create_point_base(*R_static_ebrows_root.getChildren(), static=True)
    R_static_ebrows_rig.zero_joint
    R_static_ebrows_rig.set_parent(pm.ls('C_fk00_head_ctr')[0])


    data_save_load.load_skin_cluster(*R_static_ebrows_layers.static_geometries)

    C_static_teeth_root = pm.ls('teeth_reference_points')[0]
    C_static_teeth_layers = rigStaticLayer.StaticLayer('upper_teeth','lower_teeth', name='Cstaticeteeth')
    C_static_teeth_rig = rigSingleJoint.RigSingleJoint()
    C_static_teeth_rig.create_point_base(*C_static_teeth_root.getChildren(), static=True)
    C_static_teeth_rig.zero_joint
    C_static_teeth_rig.set_parent(pm.ls('C_fk00_head_ctr')[0])

    data_save_load.load_skin_cluster(*C_static_teeth_layers.static_geometries)

    C_static_tongue_root = pm.ls('tongue_reference_points')[0]
    C_static_tongue_layers = rigStaticLayer.StaticLayer('tongue', name='Cstaticetongue')
    C_static_tongue_rig = rigSingleJoint.RigSingleJoint()
    C_static_tongue_rig.create_point_base(*C_static_tongue_root.getChildren(), static=True)
    C_static_tongue_rig.zero_joint
    C_static_tongue_rig.set_parent(pm.ls('C_fk00_head_ctr')[0])

    data_save_load.load_skin_cluster(*C_static_tongue_layers.static_geometries)


    C_static_mouth_root = pm.ls('mouth_reference_points')[0]
    C_static_mouth_layers = rigStaticLayer.StaticLayer('main','goatee', name='Cstaticemouth')
    C_static_mouth_rig = rigSingleJoint.RigSingleJoint()
    C_static_mouth_rig.create_point_base(*C_static_mouth_root.getChildren(), static=True)
    C_static_mouth_rig.zero_joint
    C_static_mouth_rig.set_parent(pm.ls('C_fk00_head_ctr')[0])

    data_save_load.load_skin_cluster(*C_static_mouth_layers.static_geometries)

