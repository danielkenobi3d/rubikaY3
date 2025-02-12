from rigBuilds.assets.male.custom_rig import rigBiped
import pymel.core as pm


def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    geo_node = pm.ls('geo', '*_GEO_GRP', '__GEO__')[0]
    pm.parent(geo_node, 'rig')
    pm.parent('environment', 'rig')

def custom_rig():
    pass

def custom_deformers():
    delta_mush = pm.deformer('GEO_bodyRaul_00', type='deltaMush')[0]
    delta_mush.smoothingIterations.set(10)