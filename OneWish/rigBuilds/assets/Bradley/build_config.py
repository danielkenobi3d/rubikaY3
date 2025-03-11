build_order = ['source', 'rig', 'load data',  'finalize']
build = {
    'source': [
        ('Import geometry', ['rig_build.import_geometry']),
        ('Import reference points', ['rig_build.import_reference_points'])
        ],
    'rig': [
        ('build biped rig', ['rig_build.build_biped_rig']),
        ('custom rig', ['rig_build.custom_rig']),
        #('facial rig', ['rig_facial.build']),
        ],
    'load data': [
        ('load skinning', ['rig_build.load_skinning_data']),
        ('load shapes', ['rig_build.load_shapes_data'])
    ],
    'finalize': [
        ('build visibility switches', ['visibility_switches.build']),
        ('cleanup', ['rig_build.cleanup']),
        ('custom finalize', ['rig_build.custom_finalize'])
    ],
}