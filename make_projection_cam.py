import sys
import fnmatch
import hou


def main(selected_nodes):    
    nodes = [node for node in selected_nodes if node.type().name() == "mrx::mrx_Chan_Camera::1.0"]
    if not nodes:
        hou.ui.displayMessage("please select a shot camera node to continue")
        return None    
    for node in nodes:
        projector = hou.node("/obj").createNode("cam", "ProjectionCam")
        children = node.children()
        cam_children = [node for node in children if node.type().name() == "mrx::mrx_Basic_Camera::1.0"] 
        for cam_child in cam_children:
            focal = cam_child.parm("focal").evalAsString()
            resx = cam_child.parm("resx").evalAsString()
            resy = cam_child.parm("resy").evalAsString()
            if focal > 0:
                projector.parm("focal").set(focal)
                projector.parm("resx").set(resx)
                projector.parm("resy").set(resy)      
            else:
                print "fail"
                return None
    return None

selected_nodes = hou.selectedNodes()  
main(selected_nodes)
