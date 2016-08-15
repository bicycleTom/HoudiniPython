import hou

selected_node = hou.selectedNodes()

for i in selected_node:
    name = i.name()
    title = i.evalParm("enable")
    if title == 1:
        print "the button is on for %s" % name
    elif title == 0:
        print "the button is on for %s" % name
        i.parm("enable").set(1)

for i in selected_node:
    name = i.name()            
    if i.parm("matte_name") is None:
        pass
    elif i.parm("matte_name") is not None:
        matteName = i.parm("matte_name").evalAsString()
        print matteName
        i.parm("matte_name").set("m_%s" % (name))

    if i.parm("multimatte_name") is None:
        pass
    elif i.parm("multimatte_name") is not None:
        multimatteName = i.parm("multimatte_name").evalAsString()
        print multimatteName
        i.parm("multimatte_name").set("m_%s" % (name))

