GISDataList = ["schools.shp", "parcels.lyr", "westerville.mxd", "westerville.gdb"] # lista
for element in GISDataList:
	...								#pętla for
if lyr.name == "Hydrography": # jezeli cos tam jest rowne tyle i tyle to
	lyr.name = "Lakes"

arcpy.env.workspace = path #ustawia workspace w katalogu w zmiennej path





mxd = arcpy.mapping.MapDocument("CURRENT")  # przypisuje do mxd bieżący dokument mapy mxd
print(mxd.title) #drukuje tytul map document
df = arcpy.mapping.ListDataFrames(mxd)[0] # lista dataFrames, glownych zbiornikow warstw, wybieram 1
lyr = arcpy.mapping.ListLayers(mxd, "", df)[3]  # lista layersów w frejmie wybieram 4 "tu wpisuje warunki"
print lyr.name
lyr.visible = False
lyr.visible = True # ustawiam widoczną warstwe
arcpy.RefreshTOC() # odświerzam table of contest
arcpy.RefreshActiveView() #odświeżam aktywne okno mapy

mxd.save() # zapisz
mxd.saveACopy() # zapisz jako

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "City of Plains View")[0]
refLayer = arcpy.mapping.ListLayers(mxd, "Parks", df)[0]
insertLayer = arcpy.mapping.Layer(r"C:\Users\Kamil\Desktop\PYTHON\mapping\MapScripting10_0\NewParks.lyr")
arcpy.mapping.InsertLayer(df, refLayer, insertLayer, "BEFORE")

for mapDoc in arcpy.ListFiles("*.mxd"):
     print mapDoc
     mxd = arcpy.mapping.MapDocument(path + mapDoc)
     for df in arcpy.mapping.ListDataFrames(mxd):
         updateLyr = arcpy.mapping.ListLayers(mxd, "Parks", df)[0]
         arcpy.mapping.UpdateLayer(df, updateLyr, sourceLyr)
     mxd.save()
     del mxd
 del sourceLyr

import arcpy
arcpy.env.workspace = "C:/Users/Kamil/Desktop/PYTHON/arcgis/PythonGP10_0/Data/SanJuan.gdb"
FCList = arcpy.ListFeatureClasses("*Anno")
for FC in FCList:
    desc = arcpy.Describe(FC)
    print FC + ":"
    print desc.spatialReference.name, "\n"