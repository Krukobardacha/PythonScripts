#Plik bada strukture pliku GML, nazwe pola, jego typ, dlugosc i precyzje
import os
import codecs

destination = u"E:/Kkruk/DaneBezOplat/100914/punkty_adr1109"
sourcee = os.listdir(destination)
for f in sourcee:
  if f[-4:]==".gml":
    layer = QgsVectorLayer(destination + "/"+ f, "cocoso", "ogr")
    prov = layer.dataProvider()
    fields = prov.fields()
    for field in fields:
        print( field.name() +"  "+ field.typeName() +"  "+str(field.length()) + "  "+str(field.precision()) )
