import sys
import fnmatch
import hou

selected_node = hou.selectedNodes()
nodes = [node for node in selected_node if node.type().name() == "#camera"]

def cam_projection_plate(selected_node):
    if not nodes:
        hou.ui.displayMessage("please select a shot camera node to continue")
        return None
    for node in nodes:
        projector = hou.node("/obj").createNode("cam", "ProjectionCam_" + str(int(hou.frame())) + "_" + str(0))
        null = hou.node("/obj").createNode("null", "null_render_" + str(int(hou.frame())) + "_" + str(0))
        children = node.children()
        cam_children = [node for node in children if node.type().name() == "#camera"]
        cam_trans = [node for node in children if node.name() == "mayaTransforms"]
        for cam_child in cam_children:
            focal = cam_child.parm("focal").evalAsString()
            resx = cam_child.parm("resx").evalAsString()
            resy = cam_child.parm("resy").evalAsString()
            aperture = cam_child.parm("aperture").evalAsString()
            if focal != 0:
                projector.parm("focal").set(focal)
                projector.parm("resx").set(resx)
                projector.parm("resy").set(resy)
                projector.parm("aperture").set(aperture)      
            else:
                print "failed to find focal"
                return None
        for cam_child in cam_trans:
            pos = cam_child.parmTuple("t").eval()
            rot = cam_child.parmTuple("r").eval()
            if pos != 0:
                projector.parmTuple("t").set(pos)
                projector.parmTuple("r").set(rot)
                null.setParms({"renderspace" : True})
                null.setFirstInput(projector)
                null.moveToGoodPosition()
                return None
            else:
                return None
    return None

def vop_projection_plate(selected_node):
    if not nodes:
        return None
    proj_vop = hou.node("/shop").createNode("vopsurface", "ProjectionPlate_" + str(int(hou.frame())) + "_" + str(0), run_init_scripts=False)
    proj_text = proj_vop.createNode("#texture_project")
    proj_file = proj_vop.createNode("parameter", "map_path")
    proj_out = proj_vop.createNode("bind", "Ce")
    for node in nodes:
        children = node.children()
        cam_children = [node for node in children if node.type().name() == "#camera"]

        for cam_child in cam_children:
            focal = cam_child.parm("focal").evalAsString()
            resx = cam_child.parm("resx").evalAsString()
            resy = cam_child.parm("resy").evalAsString()
            aperture = cam_child.parm("aperture").evalAsString()
            if focal != 0:
                proj_text.parm("proj_focal").set(focal)
                proj_text.parm("proj_resx").set(resx)
                proj_text.parm("proj_resy").set(resy)
                proj_text.parm("proj_aperture").set(aperture)
                proj_text.parm("proj_space").set("/obj/null_render_" + str(int(hou.frame())) + "_" + str(0))
                proj_file.parm("parmtype").set(15)
                proj_file.parm("parmname").set("map_path")
                proj_file.parm("parmlabel").set("Image File")
                proj_file.parm("help").set("The texture map to project")
                proj_text.setInput(0, proj_file, 0)
                proj_out.parm("parmname").set("Ce")
                proj_out.parm("parmtype").set(17)
                proj_out.parm("exportparm").set(1)
                proj_out.setInput(0, proj_text, 0)
                proj_out.moveToGoodPosition()
                proj_text.moveToGoodPosition()
                return None      
            else:
                print "failed to find focal"
                return None
    return None

cam_projection_plate(selected_node)
vop_projection_plate(selected_node)
