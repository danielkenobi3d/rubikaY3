import pymel.core as pm
from RMPY.rig import rigSingleJoint
from RMPY.rig import rigStaticLayer
from RMPY.core import data_save_load

def build():
     #L_static_ebrows_root = pm.ls('L_eyebrows_reference_points')[0]
    L_static_ebrows_layers = rigStaticLayer.StaticLayer('eyebrows', name='Lstaticebrows')
    L_static_ebrows_rig = rigSingleJoint.RigSingleJoint()
    L_static_ebrows_rig.create_point_base('L_staticeyebrow00_reference_pnt','L_staticeyebrow01_reference_pnt','L_staticeyebrow02_reference_pnt','L_staticeyebrow03_reference_pnt','L_staticeyebrow04_reference_pnt', static=True)
    L_static_ebrows_rig.zero_joint

    data_save_load.load_skin_cluster(*L_static_ebrows_layers.static_geometries)


