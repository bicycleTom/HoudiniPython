def checkAllUnderParent(parent, method, condition, optionalArgs):
    returnData = []
    children = parent.children()
    for child in children:
        if not optionalArgs:
            result = method(child)
        else:
            result = method(child, optionalArgs)
        if result == condition:
            returnData.append((child, result))
    return returnData
  
def getAttrMultiple(node, methods):
    lenMethods = len(methods)
    for method in methods:
        result = getattr(node, method)
        if lenMethods != 1:
            remainingMethods = methods[1:]
            result = getAttrMultiple(result(), remainingMethods)
            break
        else:
            return result()
    return result

def _insert_node(node, before_node=None, after_node=None, in_index=0):
   """
   Insert passed node before or after another passed node.
   """

   if not before_node and not after_node:
      log.info('Nowhere to insert %s to.' % node.path())
      return False

   if before_node:
      log.debug('Inserting %s before %s' % (node.path(), before_node.path()))
      before_node_input = None
      before_node_inputs = before_node.inputs()
      if not before_node_inputs:
         return False
      before_node_input = before_node_inputs[0]

      node.setInput(in_index, before_node_input)
      before_node.setInput(in_index, node)
      return True

   if after_node:
      log.debug('Inserting %s after %s' % (node.path(), after_node.path()))
      after_node_output = None
      after_node_outputs = after_node.outputs()
      if not after_node_outputs:
         node.setInput(in_index, after_node)
         return True

      after_node_output = after_node_outputs[0]

      after_node_output.setInput(in_index, node)
      node.setInput(in_index, after_node)
      return True

   return False


def obj_unhide(node, *args, **kwargs):
   hou.setUpdateMode(hou.updateMode.Manual)

   attr_unhide = node.createNode('attribwrangle', 'obj_unhide')
   group = attr_unhide.parmTemplateGroup()
   folder = group.findFolder("Code")
   geo_group_template = hou.StringParmTemplate("geo_group", "Geo Group", 1, default_value=([""]))
   folder.addParmTemplate(geo_group_template)
   group.appendToFolder("Code", geo_group_template)
   attr_unhide.setParmTemplateGroup(group)
   attr_unhide.parm('class').set(1)
   attr_unhide.parm('snippet').set("s@path; \
\nstring geo_grp = chs(\"geo_group\"); \
\nstring group = \"LOWPOLY\"; \
\nint condition = (int(match(geo_grp, @path))) ? 1: 0; \
\nsetprimgroup(geoself(), group, @ptnum, condition); \
\nsetprimintrinsic(geoself(),\'abcusevisibility\',@ptnum, 1,\"set\"); \
\nif(int(match(geo_grp, @path))){ \
\n    setprimintrinsic(geoself(),\'abcusevisibility\', @ptnum, 0, \"set\"); \
\n    addpoint(0, set(@P.x, @P.y-.02, @P.z+0.005)); \
\n}")
   attr_unhide.parm('geo_group').set("`chs(\"group\")`")
   attr_unhide.moveToGoodPosition()

   abc_children = [x for x in node.children() if x.type().name() in ('alembic',)]
   after_node = abc_children[0]
