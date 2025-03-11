from RMPY.rig.switches import rigEnumSwitch
import pymel.core as pm

def build():
    rig_enum_names = rigEnumSwitch.RigEnumSwitch(control='C_root00_eyes_ctr')
    rig_enum_names.add_enum_names('shineA', 'shineB', 'shineC','heart', 'heartSide', 'heartSideBroken', attribute_name='specEye')

    rig_enum_names.switch['shineA'].attribute_output >> pm.Attribute('L_shineA_spec_msh.visibility')
    rig_enum_names.switch['shineA'].attribute_output >> pm.Attribute('R_shineA_spec_msh.visibility')

    rig_enum_names.switch['shineB'].attribute_output >> pm.Attribute('L_shineB_spec_msh.visibility')
    rig_enum_names.switch['shineB'].attribute_output >> pm.Attribute('R_shineB_spec_msh.visibility')

    rig_enum_names.switch['shineC'].attribute_output >> pm.Attribute('L_shineC_spec_msh.visibility')
    rig_enum_names.switch['shineC'].attribute_output >> pm.Attribute('R_shineC_spec_msh.visibility')

    rig_enum_names.switch['heart'].attribute_output >> pm.Attribute('L_heart_spec_msh.visibility')
    rig_enum_names.switch['heart'].attribute_output >> pm.Attribute('R_heart_spec_msh.visibility')

    rig_enum_names.switch['heartSide'].attribute_output >> pm.Attribute('L_sideHeart_spec_msh.visibility')
    rig_enum_names.switch['heartSide'].attribute_output >> pm.Attribute('R_sideHeart_spec_msh.visibility')

    rig_enum_names.switch['heartSideBroken'].attribute_output >> pm.Attribute('L_sideHeartBroken_spec_msh.visibility')
    rig_enum_names.switch['heartSideBroken'].attribute_output >> pm.Attribute('R_sideHeartBroken_spec_msh.visibility')