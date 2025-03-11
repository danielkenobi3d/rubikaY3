from rigBuilds.assets.male.custom_rig import rigBiped
from rigBuilds.assets.Bradley.custom_rig import face_ctrls
from rigBuilds.assets.Bradley.custom_rig import eyes_ref
import pymel.core as pm
import importlib
importlib.reload(face_ctrls)


def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')

def custom_rig():
    face_ctrls.build()
    #eyes = eyes_ref.RigByped()