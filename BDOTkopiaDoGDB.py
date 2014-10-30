import arcpy
from arcpy import env
import os

path = "//sonas-fotka.intranet/GBDOT_BDOT10k/BDOT10k/SHAPEFILE"
#"E:/Kkruk/PROBKA_DANYCH_BDOT10k/SHAPEFILE"
source = os.listdir(path)
inFeatures = ""
inFeatures2 = ""
inFeatures3 = ""
inFeatures4 = ""
inFeatures5 = ""
inFeatures6 = ""
inFeatures7 = ""
inFeatures8 = ""
joinTable = ""
joinTable2 = ""
joinTable3 = ""
outLocation = "F:/Kkruk/Output/"
try:
    for g in source:
        if g[:-4] != ".zip":
            if not os.path.exists(outLocation+g+".gdb"):
                path2 = path + '/' + g
                c = os.listdir(path2)
                env.workspace = path2
                for s in c:
                    if s[-10:] == "SKJZ_L.shp":
                        inFeatures = s
                    if s[-10:] == "SWRS_L.shp":
                        inFeatures2 = s
                    if s[-10:] == "PTWP_A.shp":
                        inFeatures3 = s
                    if s[-12:] == "OT_Ulica.dbf":
                        joinTable = s
                    if s[-11:] == "OT_Ciek.dbf":
                        joinTable2 = s
                    if s[-20:] == "OT_ZbiornikWodny.dbf":
                        joinTable3 = s
                    if s[-10:] == "BUBD_A.shp":
                        inFeatures4 = s
                    if s[-10:] == "KUMN_A.shp":
                        inFeatures5 = s
                    if s[-10:] == "ADMS_P.shp":
                        inFeatures6 = s
                    if s[-10:] == "ADMS_A.shp":
                        inFeatures7 = s
                    if s[-10:] == "PTLZ_A.shp":
                        inFeatures8 = s
                arcpy.CreateFileGDB_management(outLocation, g+".gdb", "CURRENT")
                gdb = outLocation + g + ".gdb"
                arcpy.CopyFeatures_management(inFeatures, gdb + "/" + inFeatures[:-4])
                arcpy.CopyFeatures_management(inFeatures2, gdb + "/" + inFeatures2[:-4])
                arcpy.CopyFeatures_management(inFeatures4, gdb + "/" + inFeatures4[:-4])
                arcpy.CopyFeatures_management(inFeatures5, gdb + "/" + inFeatures5[:-4])
                arcpy.CopyFeatures_management(inFeatures6, gdb + "/" + inFeatures6[:-4])
                arcpy.CopyFeatures_management(inFeatures7, gdb + "/" + inFeatures7[:-4])
                arcpy.CopyFeatures_management(inFeatures8, gdb + "/" + inFeatures8[:-4])
                arcpy.TableToGeodatabase_conversion([joinTable, joinTable2], gdb)
                if joinTable3 == "":
                    arcpy.CopyFeatures_management(inFeatures3, gdb + "/" + inFeatures3[:-4])
                else:
                    arcpy.CopyFeatures_management(inFeatures3, gdb + "/" + inFeatures3[:-4])
                    arcpy.TableToGeodatabase_conversion(joinTable3, gdb)
                print("przekopiowalem pliki do geobazy w: " + g)
                inFeatures = ""
                inFeatures2 = ""
                inFeatures3 = ""
                inFeatures4 = ""
                inFeatures5 = ""
                inFeatures6 = ""
                inFeatures7 = ""
                inFeatures8 = ""
                joinTable = ""
                joinTable2 = ""
                joinTable3 = ""
except:
    print arcpy.GetMessages()
finally:
    print("Koniec pracy")
    print arcpy.GetMessages()
#if not os.path.exists(destination+files[0:4]): os.makedirs(destination+files[0:4])# jezeli folder nie istnieje to stworz taki
