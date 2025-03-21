# this the name of the geo that also has blendshapes and the blendshape should have the exact same name that the one for the body plus the name of the geo
prefix_geometry_list = ['eyebrows', 'tongue', 'upperTeeth', 'lowerTeeth']

definition = dict(
    jaw=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='body',
        control='c_jaw_ctrl',
        blendShapes=dict(jaw={'connection': 'translateY', 'value': -10},),
        attributes=dict(translateX={'type': 'float', 'min': 0, 'max': 10},),
        order=['translateY']
        ),

    kiss=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='body',
        control='c_kiss_ctrl',
        blendShapes=dict(kiss={'connection': 'translateX', 'value': 10},),
        attributes=dict(translateX={'type': 'float', 'min': 0, 'max': 10},),
        order=['translateX']
        ),
    smirk=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='body',
        control='c_smirk_ctrl',
        blendShapes=dict(smirk={'connection': 'translateX', 'value': 10},),
        attributes=dict(translateX={'type': 'float', 'min': 0, 'max': 10},),
        order=['translateX']
        ),
    happyA=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='body',
        control='c_happyA_ctrl',
        blendShapes=dict(happyA={'connection': 'translateX', 'value': 10}, ),
        attributes=dict(translateX={'type': 'float', 'min': 0, 'max': 10}, ),
        order=['translateX']
    ),
    happyB=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='body',
        control='c_happyB_ctrl',
        blendShapes=dict(happyB={'connection': 'translateX', 'value': 10}, ),
        attributes=dict(translateX={'type': 'float', 'min': 0, 'max': 10}, ),
        order=['translateX']
    ),
    EyebrowUpDown=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='eyebrows',
        control='L_browUpDown_face_ctrl',
        blendShapes=dict(LbrowsUpeyebrows={'connection': 'translateY', 'value': 10},
                         LbrowsDowneyebrows={'connection': 'translateY', 'value': -10},
                         ),
        attributes=dict(translateY={'type': 'float', 'min': -10, 'max': 10}, ),
        order=['translateY']
    ),

    EyebrowfaceUpDown=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='body',
        control='L_browUpDown_face_ctrl',
        blendShapes=dict(
                         LbrowsDown = {'connection': 'translateY', 'value': -10},
                         LbrowsUp ={'connection': 'translateY', 'value': 10},
                         ),
        attributes=dict(translateY={'type': 'float', 'min': -10, 'max': 10}, ),
        order=['translateY']
    ),

    mouthcorner=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='body',
        control='L_mouthCorner_face_ctrl',
        blendShapes=dict(LmouthcornerLipsUp={'connection': 'translateY', 'value': 10},
                         LmouthcornerLipsDown={'connection': 'translateY', 'value': -10}),
        attributes=dict(translateY={'type': 'float', 'min': -10, 'max': 10}, ),
        order=['translateY']
    ),
    EyebrowoutUpDown=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='eyebrows',
        control='L_outdownup_eyebrow_ctrl',
        blendShapes=dict(
                         LeyebrowsOutDown = {'connection': 'translateY', 'value': -10},
                         LeyebrowsOutUp ={'connection': 'translateY', 'value': 10},
                         ),
        attributes=dict(translateY={'type': 'float', 'min': -10, 'max': 10}, ),
        order=['translateY']
    ),
    EyebrowinUpDown=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='eyebrows',
        control='L_indownup_eyebrow_ctrl',
        blendShapes=dict(
                         LeyebrowsInDown = {'connection': 'translateY', 'value': -10},
                         LeyebrowsInUp ={'connection': 'translateY', 'value': 10},
                         ),
        attributes=dict(translateY={'type': 'float', 'min': -10, 'max': 10}, ),
        order=['translateY']
    ),
    EyeClosed=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='body',
        control='L_eyeclosed_face_ctrl',
        blendShapes=dict(
                         LeyesClosed = {'connection': 'translateY', 'value': -10},
                         ),
        attributes=dict(translateY={'type': 'float', 'min': -10, 'max': 0}, ),
        order=['translateY']
    ),
)