layer = iface.activeLayer() #zmiennej przypisujemy aktualna warstwe w mapie
plik = open('C:/Users/kkruk/Desktop/exceleTeryty/ParametrW.txt','r')
lista=[]
try:
    for i in plik:
            lista.append(str(i.strip()))
    print("stworzylem liste")
    for f in layer.getFeatures():#bierzemy sobie dla kazdego obiektu
        if  str(f['jpt_kod_je']) in lista:# nazwa z kolumny XSobrebu
            b=f.id() #pobiera id z aktualnego obiektu
            attrs = { 29 : "W"}
            layer.dataProvider().changeAttributeValues({ b:attrs })
#zmienia atrybuty na w danym wierszu b dodaje atrybut w kolumnie 3
finally:
    print "koniec"
    plik.close()
