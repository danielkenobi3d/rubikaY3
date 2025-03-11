from RMPY.rig import rigFacial
from RMPY.rig import rigBlendShapeControls
from builder.pipeline import environment



def build():
    env = environment.Environment()

    facial_definition = env.get_variables_from_path(environment.pipe_config.facial_definition)
    rigBlendShapeControls.RigBlendShapeControls(root='C_facialControls_reference_pnt')

    rigFacial.RigFacial(facial_definition.definition, prefix_geometry_list=facial_definition.prefix_geometry_list)


