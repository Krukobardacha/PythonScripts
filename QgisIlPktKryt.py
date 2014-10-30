layer = iface.activeLayer() #zmiennej przypisujemy aktualna warstwe w mapie
plik = open('C:/Users/kkruk/Desktop/exceleTeryty/Ilosc.txt','r')
lista=[]
lista2=[]
try:
    for i in plik:
            lista.append(str(i.strip()))
    print("stworzylem liste")
    for c in lista:
        lista2.append(str(c.strip().split(',')[0]))
    for f in layer.getFeatures():#bierzemy sobie dla kazdego obiektu
        if  str(f['jpt_kod_je']) in lista2:# nazwa z kolumny XSobrebu
            d=lista2.index(str(f['jpt_kod_je'])) 
            b=f.id() #pobiera id z aktualnego obiektu
            print b
            attrs = { 30 : lista[d].split(",")[1]}
            layer.dataProvider().changeAttributeValues({ b:attrs })
#zmienia atrybuty na w danym wierszu b dodaje atrybut w kolumnie 3
finally:
    print "koniec"
    plik.close()
