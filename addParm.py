import hou

#selected_node = hou.selectedNodes()

#group = selected_node.parmTemplateGroup()
#folder = hou.FolderParmTemplate("folder", "My Parms")
#folder.addParmTemplate(hou.FloatParmTemplate("myparm", "My Parm", 1))
#group.append(folder)
#node.setParmTemplateGroup(group)

selected_node = hou.selectedNodes()[0]

#def addParm(selected_node):


def main():
#    selected_node = hou.node("/obj").createNode("geo")
    group = selected_node.parmTemplateGroup()
#    folder = group.findFolder("Material")
#    group.appendToFolder(folder, hou.StringParmTemplate("mapd", "Diffuse Map", 1, \
#        default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, \
#        string_type=hou.stringParmType.Regular, menu_items=(["",""]), \
#        menu_labels=(["var a","var b"]), icon_names=([]), \
#        item_generator_script="", \
#        item_generator_script_language=hou.scriptLanguage.Python, \
#        menu_type=hou.menuType.Normal))

    hou_parm_template2 = hou.StringParmTemplate("mapd", "Diffuse Map", 1, \
        default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, \
        string_type=hou.stringParmType.Regular, menu_items=(["",""]), \
        menu_labels=(["var a","var b"]), icon_names=([]), \
        item_generator_script="", \
        item_generator_script_language=hou.scriptLanguage.Python, \
        menu_type=hou.menuType.Normal)

    folder = group.findFolder("Material")
    group.appendToFolder(folder, hou_parm_template2)

    #folder.addParmTemplate(hou_parm_template2)
    selected_node.setParmTemplateGroup(group)

main()


"""
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("mapg", "Gloss Map", 1, \
    default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, \
    string_type=hou.stringParmType.Regular, menu_items=(["",""]), \
    menu_labels=(["var a","var b"]), icon_names=([]), \
    item_generator_script="", \
    item_generator_script_language=hou.scriptLanguage.Python, \
    menu_type=hou.menuType.StringToggle)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("mapb", "Bump Map", 1, default_value=([""]), naming_scheme
=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["",""]), menu_labels
=(["var a","var b"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.sc
riptLanguage.Python, menu_type=hou.menuType.StringToggle)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
"""

"""
#Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj")

# Code for /obj/null1
hou_node = hou_parent.createNode("null", "null1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(11.3646, 2.15291))
hou_node.setSelectableInViewport(True)
hou_node.showOrigin(False)
hou_node.useXray(True)
hou_node.setDisplayFlag(True)
hou_node.setSelected(True)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4", "Transform", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("keeppos", "Keep position when parenting", default_value=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("pre_xform", "Pre-transform", menu_items=(["clean","cleantrans","cleanrot","cleanscales","extract","reset"]), menu_labels=(["Clean Transform","Clean Translates","Clean Rotates","Clean Scales","Extract P
re-transform","Reset Pre-transform"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template.addParmTemplate(hou_parm_template2)



# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("mapd", "Diffuse Map", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["",""]), menu_labels=(["var a","var b"]), icon_names=([])
, item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringToggle)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)

# Code for /obj/null1/mapd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/null1")
hou_parm = hou_node.parm("mapd")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)

"""
