def unique_values(table, field):
     with arcpy.da.SearchCursor(table, [field]) as cursor:
         return sorted({row[0] for row in cursor})
         
mxd = arcpy.mapping.MapDocument("CURRENT")
lista=arcpy.mapping.ListLayers(mxd)
for d in lista:
    b=unique_values(d, 'SRED_NOM_P')
    print b
