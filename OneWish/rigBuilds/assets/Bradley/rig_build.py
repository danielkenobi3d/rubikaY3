from rigBuilds.assets.male.custom_rig import rigBiped
from rigBuilds.assets.Bradley.custom_rig import face_ctrls
from rigBuilds.assets.Bradley.custom_rig import eyes_ref
from rigBuilds.assets.Bradley.custom_rig import eyes_viz_switch
import pymel.core as pm
import importlib
import maya.cmds as cmds
importlib.reload(face_ctrls)
importlib.reload(eyes_viz_switch)
importlib.reload(rigBiped)




def build_biped_rig():
    rig_biped = rigBiped.RigByped()
    rig_biped.build()
    pm.parent('geo', 'rig')
    pm.parent('environment', 'rig')


def custom_rig():
    # face_ctrls.build()
    eyes_viz_switch.build()

    # eyes = eyes_ref.RigByped()
def wrap_geo():
    proximity_node = cmds.proximityWrap(['beard', 'goatee'])
    cmds.proximityWrap(proximity_node, addDrivers='main', edit=True)
