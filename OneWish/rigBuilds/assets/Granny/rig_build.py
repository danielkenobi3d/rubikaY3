from rigBuilds.assets.Granny.custom_rig import rigBiped
from rubikaY3.OneWish.rigBuilds.assets.default_character import rig_facial
from rigBuilds.assets.Granny.custom_rig import face_ctrls

import pymel.core as pm
import importlib
importlib.reload(rigBiped)
importlib.reload(face_ctrls)



def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')

def custom_rig():
    face_ctrls.build()

if __name__=='__main__':
    build_biped_rig()