import sys
import fnmatch
import hou


def main(selected_nodes):    
    nodes = [node for node in selected_nodes if node.name() == "MyCam"]
    if not nodes:
        hou.ui.displayMessage("please select a shot camera node to continue")
        return None    
    for node in nodes:
        projector = hou.node("/obj").createNode("cam", "ProjectionCam_" + str(int(hou.frame())) + "_" + str(0))
        null = hou.node("/obj").createNode("null", "cam_locate")
        children = node.children()
        cam_children = [node for node in children if node.name() == "xform1"]
        for cam_child in cam_children:
            pos = cam_child.parmTuple("t").eval()
            if pos != 0:
                projector.parmTuple("t").set(pos)
                null.parmTuple("t").set(pos)
                null.setParms({"renderspace" : True})
                null.setFirstInput(projector)
                null.moveToGoodPosition()
#        for cam_child in cam_children:
#            focal = cam_child.parm("focal").evalAsString()
#            resx = cam_child.parm("resx").evalAsString()
#            resy = cam_child.parm("resy").evalAsString()
#            if focal != 0:
#                projector.parm("focal").set(focal)
#                projector.parm("resx").set(resx)
#                projector.parm("resy").set(resy)      
            else:
                print "fail"
                return None
    return None
    
def vop(selected_nodes):

    proj_vop = hou.node("/shop").createNode("vopsurface", "test_frame_" + str(int(hou.frame())) + "_" + str(0), run_init_scripts=False)
    proj_null = proj_vop.createNode("ctransform")
    proj_text = proj_vop.createNode("texture")
    print proj_null.parmTuple("from").eval()
    return None 

selected_nodes = hou.selectedNodes()  
main(selected_nodes)
vop(selected_nodes)
