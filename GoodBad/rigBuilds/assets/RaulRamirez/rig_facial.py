from RMPY.rig import rigFacial
from RMPY.rig import rigBlendShapeControls


def build():
    facial_rig = {
        'eyes': dict(
            type='blend_shape_definition',
            isSymetrical=True,
            baseMesh='faceRaul',
            control='L_facial00_eye_ctr',
            blendShapes=dict(LeyeCls={'connection': 'eyeclosed', 'value': 1}),
            attributes = dict(eyeclosed={'type': 'float', 'min': 0, 'max': 1}),
            order=['eyeclosed']
        )
    }
    rigBlendShapeControls.RigBlendShapeControls(root='C_facialControls_reference_pnt')
    rigFacial.RigFacail(),

build()
