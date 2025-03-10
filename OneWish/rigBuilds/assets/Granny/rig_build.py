from rigBuilds.assets.male.custom_rig import rigBiped
from OneWish.rigBuilds.assets.default_character.rig_build import facial_rig
import pymel.core as pm
import pymel.core as importlib
importlib.reload(facial_rig)

def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')

def custom_rig():
    facial_rig.build()