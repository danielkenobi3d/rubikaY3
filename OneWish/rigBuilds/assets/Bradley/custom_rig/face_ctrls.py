import pymel.core as pm
from RMPY.rig import rigSingleJoint
from RMPY.rig import rigStaticLayer
from RMPY.core import data_save_load
from RMPY.rig import rigLaces

def build():
     #L_static_ebrows_root = pm.ls('L_eyebrows_reference_points')[0]
    L_static_ebrows_layers = rigStaticLayer.StaticLayer('eyebrows', name='Lstaticebrows')
    L_static_ebrows_rig = rigSingleJoint.RigSingleJoint()
    L_static_ebrows_rig.create_point_base('L_staticeyebrow00_reference_pnt','L_staticeyebrow01_reference_pnt','L_staticeyebrow02_reference_pnt','L_staticeyebrow03_reference_pnt','L_staticeyebrow04_reference_pnt', static=True)
    L_static_ebrows_rig.zero_joint

    data_save_load.load_skin_cluster(*L_static_ebrows_layers.static_geometries)

    R_static_ebrows_root = pm.ls('R_eyebrows_reference_points')[0]
    R_static_ebrows_layers = rigStaticLayer.StaticLayer('eyebrows', name='Rstaticebrows')
    R_static_ebrows_rig = rigSingleJoint.RigSingleJoint()
    R_static_ebrows_rig.create_point_base(*R_static_ebrows_root.getChildren(), static=True)
    R_static_ebrows_rig.zero_joint

    data_save_load.load_skin_cluster(*R_static_ebrows_layers.static_geometries)

    L_static_ebrows_main_root = pm.ls('L_eyebrowsmain_reference_points')[0]
    L_static_ebrows_main_layers = rigStaticLayer.StaticLayer('main', name='Lstaticebrowsmain')
    L_static_ebrows_main_rig = rigSingleJoint.RigSingleJoint()
    L_static_ebrows_main_rig.create_point_base(*L_static_ebrows_main_root.getChildren(), static=True)
    L_static_ebrows_main_rig.zero_joint

    data_save_load.load_skin_cluster(*L_static_ebrows_main_layers.static_geometries)