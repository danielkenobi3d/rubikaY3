from RMPY.rig import rigFacial
from RMPY.rig.biped.rig import rigEyesAim
import pymel.core as pm

from builder.pipeline import environment


def build():
    env = environment.Environment()
    facial_definition = env.get_variables_from_path(environment.pipe_config.facial_definition)
    rigFacial.RigFacial(facial_definition.definition, prefix_geometry_list=facial_definition.prefix_geometry_list)
    pm.parentConstraint('C_fk00_head_ctr', 'facial_controls', mo=True)

    rig_eyes = rigEyesAim.RigEyesAim()
    rig_eyes.create_point_base(u'R_eye_reference_pnt', u'L_eye_reference_pnt', type='circle')

