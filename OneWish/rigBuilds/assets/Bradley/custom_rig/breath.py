import pymel.core as pm
from rigBuilds.assets.Bradley.custom_rig import rigSingleJoint
from RMPY.rig import rigStaticLayer
from RMPY.core import data_save_load
from RMPY.rig import rigLaces
import importlib
importlib.reload(rigSingleJoint)



def build():
    geos = ['shirt', 'main', 'underwear', 'pants']
    rig_static_layer = rigStaticLayer.StaticLayer(*geos, name='breath')
    for each, parent_point in zip(pm.ls('C_breath00_reference_grp')[0].getChildren(),
                                  pm.ls('C_forwardFK03_Spine_ctr','C_forwardFK00_Spine_ctr')):
        single_joint = rigSingleJoint.RigSingleJoint(rig_system=rig_static_layer.rig_system)
        single_joint.create_point_base(each, static=True, do_scale=True)
        single_joint.set_parent(parent_point)

    single_joint.zero_joint
    data_save_load.load_skin_cluster(*rig_static_layer.static_geometries)