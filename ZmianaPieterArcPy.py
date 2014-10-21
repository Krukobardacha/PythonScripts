import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
for lyr in arcpy.mapping.ListLayers(mxd):
    x = 3
#    x = arcpy.GetParameterAsText(0)
    if lyr.name == "InteriorSpace":
        expr = "[FLOORID] = " + str(x)
        lyr.definitionQuery = expr
    if lyr.name == "FloorplanElementArea":
        expr = "[FLOORID] = " + str(x)
        lyr.definitionQuery = expr
    if lyr.name == "ConveyanceArea":
        lyr.definitionQuery = "[KEYACCESSFLOORS] = '" + str(x) + "'"
arcpy.RefreshTOC()
# odswierzam table of contest
arcpy.RefreshActiveView()
#odswierzam aktywne okno mapy
