import pymel.core as pm
#from RMPY.rig.biped.rig import rigEyesAim
#from RMPY.rig.biped.rig import rigEyesSpaceSwitch
from RMPY.rig import rigStaticLayer
from RMPY.rig.facial import rigJaw
from RMPY.core import data_save_load

def build():
    jaw_static_layers = rigStaticLayer.StaticLayer('body', name='jaw')
    rig_jaw = rigJaw.RigJaw(rig_system=jaw_static_layers.rig_system)
    rig_jaw.create_point_base('C_jawstatic00_reference_pnt', 'C_jawstatic01_reference_pnt')
    data_save_load.load_skin_cluster(*jaw_static_layers.static_geometries)

