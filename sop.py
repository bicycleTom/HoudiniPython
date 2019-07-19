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
