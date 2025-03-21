from rigBuilds.assets.Granny.custom_rig import rigBiped
from rubikaY3.OneWish.rigBuilds.assets.default_character import rig_facial
import pymel.core as pm
import importlib
importlib.reload(rigBiped)


def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')

def custom_rig():
    pass


if __name__=='__main__':
    build_biped_rig()