from tkinter.constants import RIGHT

prefix_geometry_list = ['eyelashes','lower_teeth','upper_teeth']

definition = dict(
    left_eye=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='main',
        control='L_facial00_lids_ctr',
        blendShapes=dict(L_eye_wide={'connection': 'Wide', 'value': 10},
                         L_eye_blink={'connection': 'Blink', 'value': 10},
                         L_eye_half={'connection': 'Blink', 'value': 5},
                         L_eye_sad={'connection': 'Sad', 'value': -10},
                         L_eye_angry={'connection': 'Angry', 'value': 10},
                         L_eye_happy={'connection': 'Happy', 'value': 10},
                         ),
        attributes=dict(Wide={'type': 'float', 'min': 0, 'max': 10},
                        Blink={'type': 'float', 'min': 0, 'max': 10},
                        Sad={'type': 'float', 'min': 0, 'max': 10},
                        Angry={'type': 'float', 'min': 0, 'max': 10},
                        Happy={'type': 'float', 'min': 0, 'max': 10},
                        ),
        order=['Blink', 'Happy', 'Sad', 'Angry', 'Wide']
        ),
    left_brow=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='eyebrows',
        control='L_facial00_brow_ctr',
        blendShapes=dict(L_eyebrow_up={'connection': 'Up_Down', 'value': 10},
                         L_eyebrow_down={'connection': 'Up_Down', 'value': -10},
                         L_eyebrow_sad={'connection': 'Sad', 'value': 10},
                         ),
        attributes=dict(Up_Down={'type': 'float', 'min': -10, 'max': 10},
                        Sad={'type': 'float', 'min': 0, 'max': 10},
                        ),
        order=['Up_Down', 'Sad']
        ),
    mouth=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='main',
        control='C_facial00_mouth_ctr',
        blendShapes=dict(Mouth_frown={'connection': 'Frown', 'value': 10},
                         Mouth_Smile={'connection': 'Smile', 'value': 5},
                         Mouth_Pout={'connection': 'Pout', 'value': 10},
                         Mouth_yelling={'connection': 'Yell', 'value': 10},
                         Mouth_wide_smil={'connection': 'Smile', 'value': 10},
                         Mouth_O={'connection': 'Awe', 'value': 10},
                         Mouth_pursed_li={'connection': 'Kissy', 'value': 10},
                         Mouth_open_sad={'connection': 'Sad', 'value': 10},
                         Mouth_left={'connection': 'Left_Right', 'value': 10},
                         Mouth_right={'connection': 'Left_Right', 'value': -10},
                         mouth_up={'connection': 'Up_Down', 'value': 10},
                         Mouth_down={'connection': 'Up_Down', 'value': -10},
                         ),
        attributes=dict(Frown={'type': 'float', 'min': 0, 'max': 10},
                        Smile={'type': 'float', 'min': 0, 'max': 10},
                        Pout={'type': 'float', 'min': 0, 'max': 10},
                        Yell={'type': 'float', 'min': 0, 'max': 10},
                        Awe={'type': 'float', 'min': 0, 'max': 10},
                        Kissy={'type': 'float', 'min': 0, 'max': 10},
                        Sad={'type': 'float', 'min': 0, 'max': 10},
                        Left_Right={'type': 'float', 'min': -10, 'max': 10},
                        Up_Down={'type': 'float', 'min': -10, 'max': 10},
                        ),
        order=['Smile', 'Pout', 'Frown', 'Sad', 'Yell', 'Awe', 'Kissy', 'Left_Right','Up_Down']
        ),
    face=dict(
        type='blend_shape_definition',
        isSymetrical=False,
        baseMesh='main',
        control='C_facial00_face_ctr',
        blendShapes=dict(Face_sparkle_eye={'connection': 'Sprakly_eyes', 'value': 10},
                         Face_smile={'connection': 'Smile', 'value': 5},
                         Face_squiggle_s={'connection': 'Disgust', 'value': 10},
                         Face_Sad={'connection': 'Sad', 'value': 10},
                         Face_surprised={'connection': 'Surprised', 'value': 10},
                         ),
        attributes=dict(Sprakly_eyes={'type': 'float', 'min': 0, 'max': 10},
                        Smile={'type': 'float', 'min': 0, 'max': 10},
                        Disgust={'type': 'float', 'min': 0, 'max': 10},
                        Sad={'type': 'float', 'min': 0, 'max': 10},
                        Surprised={'type': 'float', 'min': 0, 'max': 10},
                        ),
        order=['Sprakly_eyes', 'Smile', 'Disgust', 'Sad', 'Surprised']
        ),

)

direct_blendshape = {
}
# 'character': 'C_BODY_001_HIGH'

jaw_layer = []
# u'character'


if __name__ == '__main__':
    import pymel.core as pm
    selection_list=[]
    for each_dictionary in [definition, eyes_dict]:
        for each_setup in each_dictionary.keys():
            for each_blendshape in each_dictionary[each_setup]['blendShapes'].keys():
                if not pm.objExists(each_blendshape):
                    print ('{} not found'.format(each_blendshape))
                if not pm.ls(each_blendshape)[0].getParent().name() == 'blendshapes':
                    selection_list.append(each_blendshape)
    pm.select(selection_list)


    '''
        right_eye=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='main',
        control='L_facial00_brow_ctr',
        blendShapes=dict(R_eye_wide={'connection': 'Wide', 'value': 10},
                         R_eye_blink={'connection': 'Blink', 'value': 10},
                         R_eye_half={'connection': 'Blink', 'value': 5},
                         R_eye_sad={'connection': 'Sad', 'value': -10},
                         R_eye_angry={'connection': 'Angry', 'value': 10},
                         R_eye_happy={'connection': 'Happy', 'value': 10},
                         ),
        attributes=dict(Wide={'type': 'float', 'min': 0, 'max': 10},
                        Blink={'type': 'float', 'min': 0, 'max': 10},
                        Sad={'type': 'float', 'min': 0, 'max': 10},
                        Angry={'type': 'float', 'min': 0, 'max': 10},
                        Happy={'type': 'float', 'min': 0, 'max': 10},
                        ),
        order=['Blink', 'Happy', 'Sad', 'Angry', 'Wide']
        ),
        right_brow=dict(
        type='blend_shape_definition',
        isSymetrical=True,
        baseMesh='eyebrows',
        control='L_facial00_brow_ctr',
        blendShapes=dict(R_eyebrow_up={'connection': 'Up_Down', 'value': 10},
                         R_eyebrow_down={'connection': 'Up_Down', 'value': -10},
                         R_eyebrow_sad={'connection': 'Sad', 'value': 10},
                         ),
        attributes=dict(Up_Down={'type': 'float', 'min': -10, 'max': 10},
                        Sad={'type': 'float', 'min': 0, 'max': 10},
                        ),
        order=['Up_Down', 'Sad']
        ),
        '''