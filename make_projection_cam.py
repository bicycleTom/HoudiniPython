import sys
import fnmatch
import hou

def main():
    nodes = hou.selectedNodes()
    projector = hou.node("/obj").createNode("cam", "ProjectionCam")
    if not nodes:
        print "no nodes selected, please select a camera node to continue"
        return None
    for node in nodes: 
        if node.type().name() == "cam":
            print "this IS a camera"
        else:
            print "this is NOT camera"

    projector = hou.node("/obj").createNode("cam", "ProjectionCam")
    projector.parm('focal').set(85)
    projector.parm('resx').set(2016)
    projector.parm('resy').set(1134)     




main()
