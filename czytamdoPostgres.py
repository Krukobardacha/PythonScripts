from itertools import takewhile
import xlrd
import codecs
#funkcja liczaca ile jest wierszy w danej kolumnie zapelnionych
def column_len(sheet, index):
    col_values = sheet.col_values(index) #Returns a sequence of the Cell objects in the given column.
    col_len = len(col_values) #dlugosc col_values
    for _ in takewhile(lambda x: not x, reversed(col_values)):
        col_len -= 1
    return col_len

workbook = xlrd.open_workbook('joze3.xls',encoding_override='utf-8')
ark= workbook.sheet_names()

for n in ark:
    sheet = workbook.sheet_by_name(n) #we can pull by name
    rows=sheet.nrows #ilosc wierszy w arkuszu
    colu=sheet.ncols #ilosc kolumn w arkuszu
    lista=[]
    print ("Dla arkusza %s :" %n)
    print ("wierszy w arkuszu %s" %rows)
    print ("kolumn w arkuszu %s" %colu)
    #print column_len(sheet, 1)
    #for g in colu:
    for x in range(1,colu):
        dlkol=column_len(sheet,x)
        if x %2 == 1:
            for wier in range(1,dlkol):
                lista.append(sheet.cell_value(wier,x))
        lista = list(set(lista))  #tworzy unikatowa liste wartosci dla danych kolumn
    else:
        print 'Final'
    print(len(lista))
    print lista[0]
    plik = codecs.open((n+".txt"), 'w', "utf-8")
    for i in range(0, len(lista)):
                buff = lista[i]+"\n"
                plik.write(buff)
    plik.close() # zapisuje liste  w pliku

#sheet.rowx
 #Returns a sequence of the Cell objects in the given row.
#col(colx) Returns a sequence of the Cell objects in the given column.
#sheet.row_len(11) zwraca liczbe kolumn w wierszu
#r = sheet.row(0) #returns all the CELLS of row 0,
#c = sheet.col_values(0) #returns all the VALUES of row 0,

#data = [] #make a data store
#for i in xrange(sheet.nrows):
#  data.append(sheet.row_values(i)) #drop all the values in the rows into data

 #if sheet.col(0)[1] returns a cell with 'number:2.0'
#sheet.col(0)[1] + 2 # will throw a TypeError.
#sheet.col(0)[1].value + 2 #will yield the expected 4.0

#sheet = book.sheet_by_index(0) or by the index it has in excel's sheet collection
#sheet = book.sheets()[0] #book.sheets() returns a list of sheet objects... alternatively...