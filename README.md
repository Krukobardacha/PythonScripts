#skrypt listujacy warstwy w arcgis, ich liczbe atrybutów, listujacy ich nazwy atrybutow i podajacy pierwszy rekord oraz typ
import arcpy
import codecs

mxd = arcpy.mapping.MapDocument("CURRENT")
lista=arcpy.mapping.ListLayers(mxd)
for d in lista:
#    listafi=[]
    fields = arcpy.ListFields(d)
    print('------------------')
    print(d)
    print(arcpy.GetCount_management(d))
    print('------------------')
    for fi in fields:
        cursor = arcpy.SearchCursor(d)
        try:
            row = cursor.next()
            a = row.getValue(fi.name)
            print(d)
            print(fi.name)
            print(a)
            print(fi.type)
            print('...')
#if a != '<Null>':      ///u'Wartosc'   text.encode('utf-8')
#            print(fi.name + a.encode('CP-1250') + fi.type)
        except(AttributeError):
            pass
