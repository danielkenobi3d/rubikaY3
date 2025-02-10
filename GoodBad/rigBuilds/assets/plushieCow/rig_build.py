from rigBuilds.assets.male.custom_rig import rigBiped
import pymel.core as pm


def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    geo_node = pm.ls('geo', '*_GEO_GRP', '__GEO__')[0]
    pm.parent(geo_node, 'rig')
    pm.parent('environment', 'rig')